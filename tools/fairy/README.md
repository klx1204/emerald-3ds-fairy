# Fairy tooling

`data.py` holds the Fairy type's data:

- `MOVES`: the seven new moves (stats, effect, target, flags, contest data).
- `RETYPE_MOVES`: Charm, Sweet Kiss and Moonlight.
- `SPECIES_TYPES`: the 18 Gen 6 retcons among the original 386.
- `TYPE_CHART`: the 12 non-1× Gen 6 chart entries.
- `LEVEL_UP` and `EGG_MOVES`: the Gen 6 `6L` / `6E` entries.

`apply.py` writes those tables into a bootstrapped pokeemerald tree and
generates the graphics: the summary badge is redrawn from the game's own
Water badge (same shape, border and font), and the menu label is adapted from
CFRU's `Type_Icons.bmp`.

```bash
python3 tools/fairy/apply.py --tree build/upstream \
    --cfru /path/to/Complete-Fire-Red-Upgrade
```

The script is idempotent for text tables. The generated pokeemerald changes
are exported as `patches/pokeemerald/0900-fairy.patch`; the port-side palette
entry lives in `3ds_port/src/3ds_bottom_ui.c`.

Move stats and learnsets come from Pokémon Showdown's Gen 6 data. No level
or egg move is invented: if a move has no `6L`/`6E` entry for a Gen 3 species,
it is not added. Dazzling Gleam is TM-only in Gen 6 and is therefore present
as data but not learnable. Light of Ruin is intentionally excluded.

See `docs/FAIRY.md` for the full scope and known limitations.
