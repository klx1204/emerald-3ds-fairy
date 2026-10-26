# Fairy type

This fork adds the Fairy type to Emerald 3DS.  It is based on the upstream
0.4.0 release and is currently **English-only**.

## Scope

- **Type 18.** `TYPE_FAIRY` is appended after `TYPE_DARK` so existing type
  numbers and save data keep their meaning.  `NUMBER_OF_MON_TYPES` becomes 19.
- **Gen 6 chart.**
  - Fairy deals 2× to Fighting, Dragon and Dark; ½× to Fire, Poison and Steel.
  - Fairy takes 2× from Poison and Steel; ½× from Fighting, Bug and Dark;
    0× from Dragon.
- **18 Gen 6 retcons** among the original 386:
  Cleffa/Clefairy/Clefable, Igglybuff/Jigglypuff/Wigglytuff, Mr. Mime,
  Snubbull/Granbull, Ralts/Kirlia/Gardevoir, Mawile, Azurill/Marill/Azumarill
  and Togepi/Togetic.
- **Charm, Sweet Kiss and Moonlight** are Fairy moves.
- **Seven new moves** (IDs 355–361).  Light of Ruin is deliberately not
  included.

## New moves

| Move | Type | Category | Power | Accuracy | PP | Effect |
|---|---|---|---|---|---|---|
| FAIRY WIND | Fairy | Special | 40 | 100 | 30 | Damage |
| MOONBLAST | Fairy | Special | 95 | 100 | 15 | 30% chance to lower Sp. Atk |
| PLAY ROUGH | Fairy | Physical* | 90 | 90 | 10 | 10% chance to lower Attack |
| DAZZLE GLEAM | Fairy | Special | 80 | 100 | 10 | Hits both foes |
| DISARM VOICE | Fairy | Special | 40 | — | 15 | Never misses; hits both foes |
| DRAIN KISS | Fairy | Special | 50 | 100 | 10 | Heals 50% of damage dealt** |
| BABY-DOLL | Fairy | Status | — | 100 | 30 | Priority +1; lowers Attack |

\* Play Rough is physical only when the optional physical/special split is
enabled.  Under the default Gen 3 rules, Fairy moves are special.

\** Gen 6's Draining Kiss heals 75%; this fork uses Emerald's existing
`EFFECT_ABSORB`, which heals 50%.

Dazzling Gleam is present as move data but has no learnset entries: in Gen 6
it is TM-only, and this fork does not add TMs.  It is therefore unobtainable
until a TM or tutor is added.

## Learnsets

Levels and egg moves are taken from the Gen 6 tags (`6L`, `6E`) in
Pokémon Showdown's `data/learnsets.ts`; nothing is invented.  The additions
cover the Fairy retcons and other Gen 3 Pokémon that learn these moves in
Gen 6 (for example Hoppip/Skiploom/Jumpluff learn Fairy Wind, Swablu/Altaria
learn Moonblast, and Skitty learns Disarming Voice).

- Level-up: Fairy Wind, Moonblast, Play Rough, Disarming Voice, Draining
  Kiss and Baby-Doll Eyes.
- Egg moves: Play Rough (Teddiursa, Phanpy, Poochyena, Absol) and Disarming
  Voice (Pichu, Whismur).

## Data sources

| Data | Source |
|---|---|
| Move stats, effects, targets | Pokémon Showdown `data/moves.ts` (Gen 6 values; checked against the Gen 6 mod) |
| Learnsets | Pokémon Showdown `data/learnsets.ts`, tags `6L` and `6E` |
| Species types | Pokémon Showdown `data/pokedex.ts` |
| Type chart | Pokémon Showdown `data/typechart.ts`, cross-checked with CFRU and PokeAPI |
| Icon/label artwork | CFRU `graphics/Other/Type_Icons/Type_Icons.bmp`, remapped to the GBA type palettes |

## Regenerating

The data lives in `tools/fairy/data.py`.  After `tools/bootstrap.py` has
created `build/upstream`, run:

```bash
python3 tools/fairy/apply.py --tree build/upstream \
    --cfru /path/to/Complete-Fire-Red-Upgrade
```

The script is idempotent for the text tables and regenerates the two PNGs.
The resulting pokeemerald changes are committed in
`patches/pokeemerald/0900-fairy.patch`; the port-side palette entry is in
`3ds_port/src/3ds_bottom_ui.c`.

## Known limitations

- **English-only.**  `tools/locales/{spanish,french,italian}.json.gz` pin the
  SHA-256 and byte offsets of the patched sources.  Adding Fairy changes those
  files, so the three localized builds need their manifests regenerated.
- **Dazzling Gleam is unobtainable** without its Gen 6 TM.
- **Draining Kiss heals 50%**, not 75%.
- The type icon is adapted from CFRU.  CFRU's terms forbid selling the game
  or soliciting donations for it; this fork is non-commercial.
- Reused battle animations: Fairy Wind uses Gust, Moonblast uses Swift, Play
  Rough uses Slam, Dazzling Gleam uses Flash, Disarming Voice uses Growl,
  Draining Kiss uses Absorb and Baby-Doll Eyes uses Charm.  Dedicated
  animations can replace them later.
