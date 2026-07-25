#!/usr/bin/env python3
"""Run dependency-free structural checks for this documentation repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "LICENSE",
    "hardware.yaml",
    "docs/architecture.md",
    "docs/compatibility.md",
    "docs/interfaces-and-wiring.md",
    "docs/power-and-mass-budget.md",
    "docs/px4-integration.md",
    "docs/bringup-and-test-plan.md",
    "docs/open-questions.md",
    "references/README.md",
]
LINK_RE = re.compile(r"!?(?:\[[^]]*\])\(([^)]+)\)")


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED:
        path = ROOT / relative
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"missing or empty required file: {relative}")

    markdown_files = sorted(ROOT.rglob("*.md"))
    for source in markdown_files:
        text = source.read_text(encoding="utf-8")
        if "\r\n" in text:
            errors.append(f"CRLF line endings: {source.relative_to(ROOT)}")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            local_part = unquote(target.split("#", 1)[0])
            if not local_part:
                continue
            resolved = (source.parent / local_part).resolve()
            if ROOT not in resolved.parents and resolved != ROOT:
                errors.append(
                    f"link escapes repository: {source.relative_to(ROOT)} -> {target}"
                )
            elif not resolved.exists():
                errors.append(
                    f"broken local link: {source.relative_to(ROOT)} -> {target}"
                )

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(markdown_files)} Markdown files and {len(REQUIRED)} required paths.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
