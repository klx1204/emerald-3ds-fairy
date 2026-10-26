#!/usr/bin/env python3
"""Apply the Fairy patch to a bootstrapped pokeemerald tree.

Usage:
    python tools/fairy/apply.py --tree build/upstream \
        --cfru /path/to/Complete-Fire-Red-Upgrade

The script is intentionally data-driven: move stats, Gen 6 learnsets and the
type chart live in data.py.  It only touches the files it must, and it is
safe to run twice (already-applied edits are skipped).
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from data import (
    EGG_MOVES,
    LEVEL_UP,
    MOVES,
    RETYPE_MOVES,
    SPECIES_TYPES,
    TYPE_CHART,
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, what: str) -> str:
    if old not in text:
        raise SystemExit("apply: cannot find %s" % what)
    return text.replace(old, new, 1)


def insert_before(text: str, marker: str, addition: str, what: str) -> str:
    if marker not in text:
        raise SystemExit("apply: cannot find marker for %s" % what)
    return text.replace(marker, addition + marker, 1)


def move_block(move: dict) -> str:
    flags = " | ".join(move["flags"])
    return (
        "    [%s] =\n"
        "    {\n"
        "        .effect = %s,\n"
        "        .power = %d,\n"
        "        .type = TYPE_FAIRY,\n"
        "        .accuracy = %d,\n"
        "        .pp = %d,\n"
        "        .secondaryEffectChance = %d,\n"
        "        .target = %s,\n"
        "        .priority = %d,\n"
        "        .flags = %s,\n"
        "    },\n\n"
        % (
            move["const"],
            move["effect"],
            move["power"],
            move["accuracy"],
            move["pp"],
            move["secondary"],
            move["target"],
            move["priority"],
            flags,
        )
    )


def apply_type_system(tree: Path) -> None:
    path = tree / "include/constants/pokemon.h"
    text = read(path)
    if "#define TYPE_FAIRY" not in text:
        text = replace_once(
            text,
            "#define TYPE_DARK             17\n#define NUMBER_OF_MON_TYPES   18",
            "#define TYPE_DARK             17\n#define TYPE_FAIRY            18\n#define NUMBER_OF_MON_TYPES   19",
            "type constants",
        )
        write(path, text)

    path = tree / "src/battle_main.c"
    text = read(path)
    if "TYPE_FAIRY, TYPE_FIGHTING" not in text:
        rows = "".join(
            "    %s, %s, %s,\n" % (att, deff, mult)
            for att, deff, mult in TYPE_CHART
        )
        text = insert_before(
            text,
            "    TYPE_FORESIGHT, TYPE_FORESIGHT, TYPE_MUL_NO_EFFECT,\n",
            rows,
            "type chart",
        )
    if '[TYPE_FAIRY] = _("FAIRY")' not in text:
        text = replace_once(
            text,
            '    [TYPE_DARK] = _("DARK"),\n',
            '    [TYPE_DARK] = _("DARK"),\n    [TYPE_FAIRY] = _("FAIRY"),\n',
            "gTypeNames",
        )
    write(path, text)

    path = tree / "src/battle_message.c"
    text = read(path)
    if "[TYPE_FAIRY]" not in text:
        text = re.sub(
            r'(\[TYPE_DARK\]\s*=\s*_\("a DARK move"\))\s*\n',
            r'\1,\n    [TYPE_FAIRY] = _("a FAIRY move"),\n',
            text,
            count=1,
        )
        if "[TYPE_FAIRY]" not in text:
            raise SystemExit("apply: cannot add Fairy to sATypeMove_Table")
    write(path, text)

    path = tree / "src/pokemon_summary_screen.c"
    text = read(path)
    if "sSpriteAnim_TypeFairy" not in text:
        text = replace_once(
            text,
            "static const union AnimCmd sSpriteAnim_CategoryCool[] = {",
            "static const union AnimCmd sSpriteAnim_TypeFairy[] = {\n"
            "    ANIMCMD_FRAME(TYPE_FAIRY * 8, 0, FALSE, FALSE),\n"
            "    ANIMCMD_END\n"
            "};\n"
            "static const union AnimCmd sSpriteAnim_CategoryCool[] = {",
            "summary animation",
        )
        text = replace_once(
            text,
            "    sSpriteAnim_TypeDark,\n    sSpriteAnim_CategoryCool,",
            "    sSpriteAnim_TypeDark,\n    sSpriteAnim_TypeFairy,\n    sSpriteAnim_CategoryCool,",
            "summary animation table",
        )
        text = replace_once(
            text,
            "    [TYPE_DARK] = 13,\n",
            "    [TYPE_DARK] = 13,\n    [TYPE_FAIRY] = 14,\n",
            "summary palette table",
        )
    write(path, text)

    path = tree / "src/menu.c"
    text = read(path)
    if "[TYPE_FAIRY + 1]" not in text:
        text = replace_once(
            text,
            "    [TYPE_DARK + 1]     = { 32, 12, 0x8C },\n",
            "    [TYPE_DARK + 1]     = { 32, 12, 0x8C },\n"
            "    [TYPE_FAIRY + 1]    = { 32, 12, 0x100 },\n",
            "menu info icons",
        )
    if "128, 144, x, y" not in text:
        text = replace_once(
            text,
            ", 0, 0, 128, 128, x, y,",
            ", 0, 0, 128, 144, x, y,",
            "menu info source height",
        )
    write(path, text)

    path = tree / "src/pokedex.c"
    text = read(path)
    if "gTypeNames[TYPE_FAIRY]" not in text:
        start = text.index("static const struct SearchOptionText sDexSearchTypeOptions")
        end = text.index("};", start)
        block = text[start:end]
        block = block.replace(
            "    {},\n",
            "    {gText_DexEmptyString, gTypeNames[TYPE_FAIRY]},\n    {},\n",
            1,
        )
        text = text[:start] + block + text[end:]
        start = text.index("static const u8 sDexSearchTypeIds")
        end = text.index("};", start)
        block = text[start:end]
        block = block.replace("    TYPE_DARK,\n", "    TYPE_DARK,\n    TYPE_FAIRY,\n", 1)
        text = text[:start] + block + text[end:]
    write(path, text)

    path = tree / "src/data/union_room.h"
    text = read(path)
    if "gTypeNames[TYPE_FAIRY]" not in text:
        text = replace_once(
            text,
            "    { sText_Exit,                NUMBER_OF_MON_TYPES }",
            "    { gTypeNames[TYPE_FAIRY],   TYPE_FAIRY         },\n"
            "    { sText_Exit,                NUMBER_OF_MON_TYPES }",
            "trading board fairy entry",
        )
    write(path, text)


def apply_species_types(tree: Path) -> None:
    path = tree / "src/data/pokemon/species_info.h"
    text = read(path)
    for species, types in SPECIES_TYPES.items():
        pattern = re.compile(
            r"(\[SPECIES_%s\]\s*=\s*\{.*?\.types\s*=\s*\{)([^}]*)(\})" % species,
            re.S,
        )
        match = pattern.search(text)
        if not match:
            raise SystemExit("apply: species block not found: " + species)
        new = "%s, %s" % types
        if match.group(2).strip() == new:
            continue
        text = text[: match.start(2)] + new + text[match.end(2) :]
    write(path, text)


def apply_moves(tree: Path) -> None:
    path = tree / "include/constants/moves.h"
    text = read(path)
    if "MOVE_FAIRY_WIND" not in text:
        defines = "".join("#define %s %d\n" % (m["const"], m["id"]) for m in MOVES)
        text = replace_once(
            text,
            "#define MOVES_COUNT 355",
            defines + "\n#define MOVES_COUNT 362",
            "move constants",
        )
    write(path, text)

    path = tree / "src/data/battle_moves.h"
    text = read(path)
    for const, new_type in RETYPE_MOVES.items():
        pattern = re.compile(r"(\[%s\]\s*=\s*\{.*?\.type\s*=\s*)(TYPE_\w+)" % const, re.S)
        match = pattern.search(text)
        if not match:
            raise SystemExit("apply: retype move not found: " + const)
        if match.group(2) != new_type:
            text = text[: match.start(2)] + new_type + text[match.end(2) :]
    if "[MOVE_FAIRY_WIND]" not in text:
        text = insert_before(text, "};", "".join(move_block(m) for m in MOVES), "battle moves")
    write(path, text)

    path = tree / "src/data/text/move_names.h"
    text = read(path)
    if "[MOVE_FAIRY_WIND]" not in text:
        names = "".join('    [%s] = _("%s"),\n' % (m["const"], m["name"]) for m in MOVES)
        text = insert_before(text, "};", names, "move names")
    write(path, text)

    path = tree / "src/data/text/move_descriptions.h"
    text = read(path)
    if "sFairyWindDescription" not in text:
        strings = ""
        for m in MOVES:
            camel = "".join(part.capitalize() for part in m["const"][5:].lower().split("_"))
            strings += (
                "static const u8 s%sDescription[] = _(\n"
                '    "%s");\n\n' % (camel, m["desc"])
            )
        marker = "const u8 *const gMoveDescriptionPointers[MOVES_COUNT - 1] ="
        text = replace_once(text, marker, strings + marker, "move descriptions")
        start = text.index(marker)
        end = text.index("};", start)
        pointers = ""
        for m in MOVES:
            camel = "".join(part.capitalize() for part in m["const"][5:].lower().split("_"))
            pointers += "    [%s - 1] = s%sDescription,\n" % (m["const"], camel)
        text = text[:end] + pointers + text[end:]
    write(path, text)

    path = tree / "src/data/move_categories.h"
    text = read(path)
    if "[MOVE_FAIRY_WIND]" not in text:
        cats = "".join(
            "    [%s] = %s,\n" % (m["const"], m["category"]) for m in MOVES
        )
        text = insert_before(text, "};", cats, "move categories")
    write(path, text)

    path = tree / "src/data/contest_moves.h"
    text = read(path)
    if "[MOVE_FAIRY_WIND]" not in text:
        start = text.index("const struct ContestMove gContestMoves[MOVES_COUNT]")
        end = text.index("\n};", start)
        entries = ""
        for m in MOVES:
            effect, category = m["contest"]
            entries += (
                "    [%s] =\n"
                "    {\n"
                "        .effect = %s,\n"
                "        .contestCategory = %s,\n"
                "        .comboStarterId = 0,\n"
                "        .comboMoves = {0},\n"
                "    },\n\n" % (m["const"], effect, category)
            )
        text = text[:end] + "\n" + entries + text[end:]
    write(path, text)

    path = tree / "data/battle_anim_scripts.s"
    text = read(path)
    if "// Fairy moves" not in text:
        anims = "// Fairy moves\n" + "".join("\t.int %s\n" % m["anim"] for m in MOVES)
        text = insert_before(text, "\t.int Move_COUNT /*", anims, "move animations")
    write(path, text)


def insert_level_up(text: str, species: str, level: int, move: str) -> str:
    camel = "".join(part.capitalize() for part in species.lower().split("_"))
    marker = "static const u16 s%sLevelUpLearnset[] = {\n" % camel
    if marker not in text:
        raise SystemExit("apply: learnset not found: " + species)
    start = text.index(marker) + len(marker)
    end = text.index("\n};", start)
    block = text[start:end]
    if move in block:
        return text
    lines = block.split("\n")
    new_line = "    LEVEL_UP_MOVE(%2d, %s)," % (level, move)
    insert_at = next(
        (i for i, line in enumerate(lines) if "LEVEL_UP_END" in line),
        len(lines),
    )
    for i, line in enumerate(lines):
        m = re.search(r"LEVEL_UP_MOVE\(\s*(\d+),", line)
        if m and int(m.group(1)) > level:
            insert_at = i
            break
    lines.insert(insert_at, new_line)
    return text[:start] + "\n".join(lines) + text[end:]


def apply_learnsets(tree: Path) -> None:
    path = tree / "src/data/pokemon/level_up_learnsets.h"
    text = read(path)
    for move, entries in LEVEL_UP.items():
        for species, level in entries:
            text = insert_level_up(text, species, level, move)
    write(path, text)

    path = tree / "src/data/pokemon/egg_moves.h"
    text = read(path)
    for move, species_list in EGG_MOVES.items():
        for species in species_list:
            head = "egg_moves(%s," % species
            start = text.find(head)
            if start < 0:
                raise SystemExit("apply: egg move block not found: " + species)
            end = text.index("),", start)
            block = text[start:end]
            if move in block:
                continue
            text = text[:end] + ",\n              %s" % move + text[end:]
    write(path, text)


def read_jasc(path: Path) -> list[tuple[int, int, int]]:
    lines = [line.strip() for line in read(path).splitlines() if line.strip()]
    if lines[0] != "JASC-PAL":
        raise SystemExit("apply: not a JASC palette: " + str(path))
    count = int(lines[2])
    return [tuple(int(v) for v in line.split()) for line in lines[3 : 3 + count]]


def nearest(color, palette, allow_zero=True):
    best = None
    best_d = 1 << 30
    for i, pal in enumerate(palette):
        if i == 0 and not allow_zero:
            continue
        d = sum((a - b) ** 2 for a, b in zip(color, pal))
        if d < best_d:
            best_d = d
            best = i
    return best


def map_fairy_cell(cell, palette, transparent_rgb, pink_index, white_index, dark_index, grey_index):
    from PIL import Image

    out = Image.new("P", cell.size)
    if palette is None:
        palette = cell.getpalette()
    out.putpalette(palette)
    pixels = cell.load()
    for y in range(cell.height):
        for x in range(cell.width):
            r, g, b = pixels[x, y][:3]
            if abs(r - transparent_rgb[0]) + abs(g - transparent_rgb[1]) + abs(b - transparent_rgb[2]) < 60:
                index = 0
            elif r > 225 and g > 225 and b > 225:
                index = white_index
            elif r < 90 and g < 90 and b < 90:
                index = dark_index
            elif r > 200 and b > 150 and g < 220:
                index = pink_index
            else:
                index = grey_index
            out.putpixel((x, y), index)
    return out


def make_icons(tree: Path, cfru: Path) -> None:
    from PIL import Image

    bmp = Image.open(cfru / "graphics/Other/Type_Icons/Type_Icons.bmp").convert("RGB")
    cell = bmp.crop((0, 128, 32, 144))

    # 32x16 type icon, drawn with move_types_2 (the pink/psychic palette).
    pal = read_jasc(tree / "graphics/types/move_types_2.pal")
    fairy = map_fairy_cell(cell, [v for rgb in pal for v in rgb], (120, 152, 128), 8, 10, 15, 13)
    fairy.save(tree / "graphics/types/fairy.png")

    # 32x12 menu label, appended at tile 0x100 of menu_info.png.
    menu_path = tree / "graphics/interface/menu_info.png"
    menu = Image.open(menu_path)
    if menu.mode != "P":
        menu = menu.convert("P")
    if menu.height != 144:
        label = map_fairy_cell(cell.crop((0, 0, 32, 12)), menu.getpalette(), (120, 152, 128), 12, 14, 15, 13)
        new = Image.new("P", (128, 144))
        new.putpalette(menu.getpalette())
        new.paste(menu, (0, 0))
        new.paste(label, (0, 128))
        new.save(menu_path)

    path = tree / "graphics_file_rules.mk"
    text = read(path)
    if "fairy" not in text.split("types :=", 1)[1].splitlines()[0]:
        text = replace_once(
            text,
            "types := normal fight flying poison ground rock bug ghost steel mystery fire water grass electric psychic ice dragon dark",
            "types := normal fight flying poison ground rock bug ghost steel mystery fire water grass electric psychic ice dragon dark fairy",
            "types list",
        )
    write(path, text)


def apply_port(repo: Path) -> None:
    path = repo / "3ds_port/src/3ds_bottom_ui.c"
    if not path.exists():
        return
    text = read(path)
    if "[TYPE_FAIRY]" not in text:
        text = replace_once(
            text,
            "    [TYPE_DRAGON] = 2, [TYPE_DARK] = 0,\n",
            "    [TYPE_DRAGON] = 2, [TYPE_DARK] = 0, [TYPE_FAIRY] = 1,\n",
            "bottom UI type palette",
        )
        write(path, text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tree", type=Path, default=Path("build/upstream"))
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument(
        "--cfru",
        type=Path,
        default=Path("Complete-Fire-Red-Upgrade"),
        help="path to a CFRU checkout (for graphics/Other/Type_Icons/Type_Icons.bmp)",
    )
    args = parser.parse_args()

    apply_type_system(args.tree)
    apply_species_types(args.tree)
    apply_moves(args.tree)
    apply_learnsets(args.tree)
    make_icons(args.tree, args.cfru)
    apply_port(args.repo)
    print("apply: Fairy patch applied to", args.tree)


if __name__ == "__main__":
    main()
