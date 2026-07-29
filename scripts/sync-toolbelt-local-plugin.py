#!/usr/bin/env python3
"""Copy d:\\Toolbelt → ~/.cursor/plugins/local/toolbelt (replace).

Operational load path for local Cursor plugins.

Usage (from anywhere):
  python d:\\Toolbelt\\scripts\\sync-toolbelt-local-plugin.py
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

REPO_PLUGIN = Path(r"d:\Toolbelt")
LOCAL_PLUGIN = Path.home() / ".cursor" / "plugins" / "local" / "toolbelt"


def main() -> int:
    if not (REPO_PLUGIN / ".cursor-plugin" / "plugin.json").is_file():
        print(f"FAIL: missing manifest under {REPO_PLUGIN}", file=sys.stderr)
        return 1
    LOCAL_PLUGIN.parent.mkdir(parents=True, exist_ok=True)
    if LOCAL_PLUGIN.exists():
        shutil.rmtree(LOCAL_PLUGIN)
    shutil.copytree(
        REPO_PLUGIN,
        LOCAL_PLUGIN,
        ignore=shutil.ignore_patterns(
            ".git",
            "__pycache__",
            "*.pyc",
            ".cursor",
        ),
    )
    print(f"OK synced -> {LOCAL_PLUGIN}")
    print("Next: Developer: Reload Window, then check Customize -> Plugins for toolbelt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
