#!/usr/bin/env python3
"""Copy Toolbelt docs SoT into skills/*/references/ (single source of truth).

Mapping:
  docs/PROTOCOL.md              → skills/research-protocol/references/PROTOCOL.md
  docs/templates/research-note.md → skills/research-protocol/references/research-note.md
  docs/templates/claim-citation.md → skills/research-protocol/references/claim-citation.md
  docs/templates/research-depth-modes.md → skills/research-protocol/references/research-depth-modes.md
  docs/templates/codebase-reconnaissance.md → skills/codebase-recon/references/s0-s18-checklist.md
  docs/templates/documentation-research.md → skills/docs-research/references/d0-d14-checklist.md
  docs/templates/agents-md-skeleton.md → skills/author-agents-md/references/agents-md-skeleton.md
  docs/templates/doc-layers.md → skills/author-agents-md/references/doc-layers.md
  docs/templates/adr-minimal.md → skills/draft-adr/references/adr-minimal.md
  docs/templates/author-cursor-surfaces.md → skills/author-cursor-surfaces/references/author-cursor-surfaces.md

Usage:
  python d:\\Toolbelt\\scripts\\refresh-skill-references.py
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(r"d:\Toolbelt")

COPIES: list[tuple[Path, Path]] = [
    (ROOT / "docs" / "PROTOCOL.md", ROOT / "skills" / "research-protocol" / "references" / "PROTOCOL.md"),
    (ROOT / "docs" / "templates" / "research-note.md", ROOT / "skills" / "research-protocol" / "references" / "research-note.md"),
    (ROOT / "docs" / "templates" / "claim-citation.md", ROOT / "skills" / "research-protocol" / "references" / "claim-citation.md"),
    (ROOT / "docs" / "templates" / "research-depth-modes.md", ROOT / "skills" / "research-protocol" / "references" / "research-depth-modes.md"),
    (ROOT / "docs" / "templates" / "codebase-reconnaissance.md", ROOT / "skills" / "codebase-recon" / "references" / "s0-s18-checklist.md"),
    (ROOT / "docs" / "templates" / "documentation-research.md", ROOT / "skills" / "docs-research" / "references" / "d0-d14-checklist.md"),
    (ROOT / "docs" / "templates" / "agents-md-skeleton.md", ROOT / "skills" / "author-agents-md" / "references" / "agents-md-skeleton.md"),
    (ROOT / "docs" / "templates" / "doc-layers.md", ROOT / "skills" / "author-agents-md" / "references" / "doc-layers.md"),
    (ROOT / "docs" / "templates" / "adr-minimal.md", ROOT / "skills" / "draft-adr" / "references" / "adr-minimal.md"),
    (ROOT / "docs" / "templates" / "author-cursor-surfaces.md", ROOT / "skills" / "author-cursor-surfaces" / "references" / "author-cursor-surfaces.md"),
]


def main() -> int:
    missing = [src for src, _ in COPIES if not src.is_file()]
    if missing:
        for p in missing:
            print(f"FAIL: missing SoT {p}", file=sys.stderr)
        return 1
    for src, dst in COPIES:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print(f"OK {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
