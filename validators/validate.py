from __future__ import annotations

import argparse
import json
from datetime import date, datetime
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
from pyshacl import validate as shacl_validate
from rdflib import Graph

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMAS_DIR = REPO_ROOT / "schemas"
SHACL_DIR = REPO_ROOT / "shacl"

TYPE_TO_SCHEMA = {
    "Agent": "agent.schema.json",
    "Skill": "skill.schema.json",
    "Process": "process.schema.json",
}


def normalize(value: Any) -> Any:
    if isinstance(value, datetime):
        return value.isoformat().replace("+00:00", "Z")
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, list):
        return [normalize(item) for item in value]
    if isinstance(value, dict):
        return {key: normalize(item) for key, item in value.items()}
    return value


def load_yaml(path: Path) -> Any:
    return normalize(yaml.safe_load(path.read_text(encoding="utf-8")))


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def extract_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path} is missing YAML frontmatter")
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        raise ValueError(f"{path} has malformed YAML frontmatter")
    frontmatter = normalize(yaml.safe_load(parts[0][4:]))
    if not isinstance(frontmatter, dict):
        raise ValueError(f"{path} frontmatter must be a mapping")
    return frontmatter


def iter_bundles(root: Path) -> list[Path]:
    if (root / "workiq.yaml").exists():
        return [root]
    return sorted(path.parent for path in root.rglob("workiq.yaml"))


def build_registry() -> Registry:
    registry = Registry()
    for schema_path in SCHEMAS_DIR.glob("*.json"):
        contents = load_json(schema_path)
        registry = registry.with_resource(contents["$id"], Resource.from_contents(contents))
    return registry


def make_validator(schema_name: str) -> Draft202012Validator:
    schema = load_json(SCHEMAS_DIR / schema_name)
    registry = build_registry().with_resource(str((SCHEMAS_DIR / schema_name).resolve().as_uri()), Resource.from_contents(schema))
    return Draft202012Validator(schema, registry=registry)


def validate_manifest(bundle_dir: Path) -> list[str]:
    manifest = load_yaml(bundle_dir / "workiq.yaml")
    validator = make_validator("workiq-bundle.schema.json")
    return [f"{bundle_dir}/workiq.yaml: {error.message}" for error in validator.iter_errors(manifest)]


def schema_name_for(frontmatter: dict[str, Any]) -> str:
    return TYPE_TO_SCHEMA.get(frontmatter.get("type"), "concept.schema.json")


def validate_documents(bundle_dir: Path) -> list[str]:
    errors: list[str] = []
    for path in sorted(bundle_dir.rglob("*.md")):
        frontmatter = extract_frontmatter(path)
        validator = make_validator(schema_name_for(frontmatter))
        errors.extend(f"{path}: {error.message}" for error in validator.iter_errors(frontmatter))
    return errors


def validate_exports(bundle_dir: Path) -> list[str]:
    manifest = load_yaml(bundle_dir / "workiq.yaml") or {}
    exports = manifest.get("exports", [])
    if not exports:
        return []

    shapes_graph = Graph()
    for shape_path in sorted(SHACL_DIR.glob("*.ttl")):
        shapes_graph.parse(shape_path)

    errors: list[str] = []
    for export in exports:
        export_path = bundle_dir / export["path"]
        if not export_path.exists():
            errors.append(f"{export_path}: declared export file does not exist")
            continue
        data_graph = Graph()
        data_graph.parse(export_path)
        conforms, _, report_text = shacl_validate(data_graph, shacl_graph=shapes_graph, inference="rdfs")
        if not conforms:
            errors.append(f"{export_path}: SHACL validation failed\n{report_text}")
    return errors


def validate_root(root: Path) -> list[str]:
    bundle_dirs = iter_bundles(root)
    if not bundle_dirs:
        return [f"{root}: no bundles found"]

    errors: list[str] = []
    for bundle_dir in bundle_dirs:
        errors.extend(validate_manifest(bundle_dir))
        errors.extend(validate_documents(bundle_dir))
        errors.extend(validate_exports(bundle_dir))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Work IQ Open Format bundles")
    parser.add_argument("--root", default="examples", help="Directory containing one or more bundles")
    parser.add_argument("--expect-fail", action="store_true", help="Invert success for failing fixtures")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors = validate_root(root)
    success = not errors

    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validation passed for {root}")

    if args.expect_fail:
        return 0 if not success else 1
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
