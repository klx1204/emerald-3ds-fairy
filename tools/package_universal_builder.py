#!/usr/bin/env python3
"""Package the cross-platform, source-based Emerald 3DS builder.

    python tools/package_universal_builder.py \
        --tree build/upstream \
        --recipe dist/emerald3ds.recipe \
        --out dist/Emerald3DS-Fairy-Builder-universal.zip

The payload is identical on every OS; only the launcher is different:

    run-builder.command   macOS
    run-builder.sh        Linux
    run-builder.bat       Windows

No PyInstaller executable is built.  The user needs Python 3.11+ and Pillow
(and Tk only for the window; the command line works without it).
"""

from __future__ import annotations

import argparse
import ast
import shutil
import stat
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATORS = [
    "gen_voxel_regions.py",
    "gen_voxel_sign_masks.py",
    "gen_voxel_relief.py",
    "gen_voxel_buildings.py",
    "gen_intro_margins.py",
]
VOXELGEN_FILES = ["src/voxel/voxel_regions.h", "assets/voxel/relief_fixes.json"]
EXECUTABLES = ("Emerald3DS.3dsx", "Emerald3DS.smdh")


def local_closure(scripts_dir: Path, names: list[str]) -> list[str]:
    todo = [n for n in names if (scripts_dir / n).exists()]
    seen: set[str] = set()
    while todo:
        name = todo.pop()
        if name in seen:
            continue
        seen.add(name)
        tree = ast.parse((scripts_dir / name).read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            mods: list[str] = []
            if isinstance(node, ast.Import):
                mods = [a.name for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
                mods = [node.module]
            for mod in mods:
                top = mod.split(".")[0]
                if (scripts_dir / (top + ".py")).exists():
                    todo.append(top + ".py")
    return sorted(seen)


def write(path: Path, text: str, executable: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    if executable:
        path.chmod(path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def build(tree: Path, recipe: Path, out: Path, version: str) -> None:
    port = tree / "3ds_port"
    dist = port / "dist"
    missing = [str(p) for p in (dist / "Emerald3DS.3dsx", dist / "Emerald3DS.smdh", recipe) if not p.exists()]
    if missing:
        raise SystemExit("package: missing " + ", ".join(missing) + " (run make release and generate the recipe first)")

    work = out.parent / (out.name + ".d")
    if work.exists():
        shutil.rmtree(work)
    payload = work / "payload"
    payload.mkdir(parents=True)

    for name in EXECUTABLES:
        shutil.copy2(dist / name, payload / name)
    shutil.copy2(recipe, payload / "emerald3ds.recipe")

    scripts = local_closure(port / "scripts", GENERATORS)
    (payload / "voxelgen" / "scripts").mkdir(parents=True)
    for name in scripts:
        shutil.copy2(port / "scripts" / name, payload / "voxelgen" / "scripts" / name)
    for rel in VOXELGEN_FILES:
        dst = payload / "voxelgen" / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(port / rel, dst)

    builder = work / "builder"
    shutil.copytree(
        ROOT / "builder" / "emerald3ds_builder",
        builder / "emerald3ds_builder",
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
    )
    shutil.copy2(ROOT / "builder" / "README.md", builder / "README.md")

    write(work / "requirements.txt", "Pillow>=10\n")
    # The launchers prefer a local .venv (pip installs may be refused outside
    # one on macOS and recent Linux distributions).
    write(
        work / "run-builder.sh",
        '#!/bin/sh\nset -e\ncd "$(dirname "$0")"\n'
        'export PYTHONPATH="$PWD/builder${PYTHONPATH:+:$PYTHONPATH}"\n'
        'if [ -x .venv/bin/python3 ]; then PY=.venv/bin/python3; else PY=python3; fi\n'
        'exec "$PY" -m emerald3ds_builder --payload "$PWD/payload" "$@"\n',
        executable=True,
    )
    write(
        work / "run-builder.command",
        '#!/bin/sh\nset -e\ncd "$(dirname "$0")"\n'
        'export PYTHONPATH="$PWD/builder${PYTHONPATH:+:$PYTHONPATH}"\n'
        'if [ -x .venv/bin/python3 ]; then PY=.venv/bin/python3; else PY=python3; fi\n'
        'exec "$PY" -m emerald3ds_builder --payload "$PWD/payload" "$@"\n',
        executable=True,
    )
    write(
        work / "run-builder.bat",
        "@echo off\r\ncd /d \"%~dp0\"\r\n"
        "set \"PYTHONPATH=%~dp0builder;%PYTHONPATH%\"\r\n"
        "if exist \".venv\\Scripts\\python.exe\" (\r\n"
        "  \".venv\\Scripts\\python.exe\" -m emerald3ds_builder --payload \"%~dp0payload\" %*\r\n"
        ") else (\r\n"
        "  py -3 -m emerald3ds_builder --payload \"%~dp0payload\" %*\r\n"
        ")\r\n",
    )

    readme = """Emerald 3DS Fairy Builder (universal)
=====================================

Version """ + version + """

This ZIP is the same on Windows, macOS and Linux.  It contains the builder
source, the engine executable and the recipe.  The game data is generated
from your own clean Pokemon Emerald ROM on this computer; the ROM is never
uploaded or copied.

Requirements
------------
- Python 3.11 or newer
- Pillow, in a virtual environment next to these files (recommended):

    macOS/Linux:  python3 -m venv .venv
                  .venv/bin/pip install -r requirements.txt
    Windows:      py -3 -m venv .venv
                  .venv\\Scripts\\pip install -r requirements.txt

  The launchers use .venv automatically when it exists.  Without one they
  fall back to the system python3/py -3, where you may install Pillow with
  `python3 -m pip install --user -r requirements.txt` (or your system
  package: `sudo apt install python3-pil`).
- Tk (optional, only for the window): macOS python.org/Homebrew builds have
  it; Linux needs python3-tk.  The command line works without Tk.

Run
---
macOS:   ./run-builder.command
Linux:   ./run-builder.sh
Windows: run-builder.bat

Or from a terminal:

    ./run-builder.sh          # opens the window

Command line examples:

    ./run-builder.sh build --rom "Pokemon Emerald.gba" --output out
    ./run-builder.sh install --rom "Pokemon Emerald.gba" --sd /media/me/3DS
    ./run-builder.sh verify --pak out/emerald3ds.pak

On Windows use `run-builder.bat` in place of ./run-builder.sh.

The builder writes:

    <SD>/3ds/emerald3ds/Emerald3DS.3dsx
    <SD>/3ds/emerald3ds/Emerald3DS.smdh
    <SD>/3ds/emerald3ds/emerald3ds.pak

Saves stay in <SD>/3ds/emerald3ds/emerald3ds.sav and are not touched by an
update.  A data pack only works with the engine it was built for.

This is an unofficial, non-commercial fan fork.  The Fairy menu label is
adapted from CFRU; no donations are accepted for this fork.
"""
    write(work / "README.txt", readme)

    lic = work / "LICENSES"
    lic.mkdir()
    for rel in ("LICENSE-PORT.md", "NOTICE.md", "AI_DISCLOSURE.md"):
        src = ROOT / rel
        if src.exists():
            shutil.copy2(src, lic / rel)
    voxel_notice = port / "src" / "voxel" / "NOTICE.md"
    if voxel_notice.exists():
        shutil.copy2(voxel_notice, lic / "voxel-NOTICE.md")

    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        out.unlink()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(work.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(work).as_posix())
    shutil.rmtree(work)
    print("package: %s (%.1f MiB)" % (out, out.stat().st_size / 1048576))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--tree", type=Path, default=Path("build/upstream"))
    ap.add_argument("--recipe", type=Path, default=Path("dist/emerald3ds.recipe"))
    ap.add_argument("--out", type=Path, default=Path("dist/Emerald3DS-Fairy-Builder-universal.zip"))
    ap.add_argument("--version", default="0.4.0-fairy.1")
    args = ap.parse_args()
    build(args.tree, args.recipe, args.out, args.version)
    return 0


if __name__ == "__main__":
    sys.exit(main())
