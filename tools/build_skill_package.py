#!/usr/bin/env python3
"""Build a deterministic runtime archive for the skill."""

from __future__ import annotations

import argparse
from pathlib import Path
from zipfile import ZIP_STORED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
RUNTIME_FILES = ("SKILL.md", "agents", "references", "assets", "scripts/analysis_guard.py")
ARCHIVE_ROOT = Path("governed-analytics-workflow")
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".py"}


def package_files() -> list[Path]:
    files: list[Path] = []
    for relative in RUNTIME_FILES:
        source = ROOT / relative
        if source.is_file():
            files.append(source)
        elif source.is_dir():
            files.extend(path for path in source.rglob("*") if path.is_file() and "__pycache__" not in path.parts)
    return sorted(files, key=lambda path: path.relative_to(ROOT).as_posix())


def canonical_runtime_bytes(path: Path) -> bytes:
    data = path.read_bytes()
    if path.suffix.lower() in TEXT_SUFFIXES:
        return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return data


def build(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_STORED) as archive:
        for path in package_files():
            relative = ARCHIVE_ROOT / path.relative_to(ROOT)
            info = ZipInfo(relative.as_posix(), date_time=(2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.compress_type = ZIP_STORED
            info.external_attr = 0o644 << 16
            archive.writestr(info, canonical_runtime_bytes(path))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    build(args.output)
    print(f"Created {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
