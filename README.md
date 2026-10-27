<p align="center">
  <img src="https://i.postimg.cc/XJRQB9cc/logo2.png" alt="Emerald 3DS" width="480">
</p>

<h1 align="center">Emerald 3DS</h1>

> **Unofficial Fairy fork.** This repository is `klx1204/emerald-3ds-fairy`,
> based on [ZallaxDev/emerald-3ds](https://github.com/ZallaxDev/emerald-3ds)
> 0.4.0. It adds the Fairy type, the Gen 6 Fairy retcons for the original 386
> Pokémon, and seven Gen 6 Fairy moves. It is **English-only** and not
> affiliated with or endorsed by Zallax.
>
> This fork is **non-commercial**: it includes a type icon adapted from
> Complete-Fire-Red-Upgrade (CFRU), whose terms forbid selling the game or
> soliciting donations for it. No donations are accepted for this fork.
>
> Download this fork from
> [its GitHub Releases](https://github.com/klx1204/emerald-3ds-fairy/releases).
> The upstream site (`emerald-3ds.com`) distributes the vanilla project, not
> this fork.

<p align="center">
  <strong>Rediscover Hoenn. Two screens. A new perspective.</strong><br>
  A native Nintendo 3DS port with a touch interface and an optional voxel overworld.
</p>

<p align="center">
  <a href="https://emerald-3ds.com/"><img src="https://img.shields.io/badge/Play_now-Web_builder-168B67?style=for-the-badge&amp;logo=firefoxbrowser&amp;logoColor=white" alt="Generate the latest version in your browser"></a>
  <a href="https://x.com/DustZallax"><img src="https://img.shields.io/badge/Follow-%40DustZallax-18181B?style=for-the-badge&amp;logo=x&amp;logoColor=white" alt="Follow @DustZallax on X"></a>
  <a href="https://discord.com/invite/tfqHF8496P"><img src="https://img.shields.io/badge/Discord-Join_the_community-5865F2?style=for-the-badge&amp;logo=discord&amp;logoColor=white" alt="Join the community on Discord"></a>
</p>

## Get this fork

**Download `Emerald3DS-Fairy-Builder-universal.zip` from the [latest release](https://github.com/klx1204/emerald-3ds-fairy/releases/latest), run it on Windows, macOS or Linux, and point it at your own clean English Emerald ROM.**

The ZIP contains the builder, the engine and the data recipe; the game data is generated on your computer and nothing is uploaded. See [Getting started](#getting-started) for the three commands.

> **Note:** [emerald-3ds.com](https://emerald-3ds.com/) is the upstream project's site. It builds the vanilla game, **not** this Fairy fork, but its installation guide, sound setup and FAQ apply unchanged.

<p align="center">
  <a href="#screenshots">Screenshots</a> &nbsp; · &nbsp;
  <a href="#features">Features</a> &nbsp; · &nbsp;
  <a href="https://emerald-3ds.com/">Upstream instructions &amp; FAQ</a> &nbsp; · &nbsp;
  <a href="#documentation">Documentation</a> &nbsp; · &nbsp;
  <a href="#community">Community</a>
</p>

---

Emerald 3DS brings the adventure to Nintendo 3DS as
**native homebrew**. The game runs on the top screen, while a dedicated touch
interface on the bottom screen replaces the START menu. Enable the optional
**voxel overworld** to explore supported areas from a new angle.

## Screenshots

<p align="center"><em>A look at the adventure across both screens.</em></p>

<table>
  <tr>
    <td><img src="https://i.postimg.cc/h42VQzvT/10-10-26-18-38-57-898.png" alt="Screenshot 1" width="400"></td>
    <td><img src="https://i.postimg.cc/d1BrBDBc/10-10-26-18-39-27-88.png" alt="Screenshot 2" width="400"></td>
  </tr>
  <tr>
    <td><img src="https://i.postimg.cc/bwtn5mTG/10-10-26-18-29-16-693.png" alt="Screenshot 3" width="400"></td>
    <td><img src="https://i.postimg.cc/vmwnw5qC/10-10-26-18-28-18-321.png" alt="Screenshot 4" width="400"></td>
  </tr>
</table>

<details>
<summary><strong>View more screenshots · 9 more images</strong></summary>

<br>

<table>
  <tr>
    <td><img src="https://i.postimg.cc/gj7wSh6W/10-10-26-18-27-40-122.png" alt="Screenshot 5" width="400"></td>
    <td><img src="https://i.postimg.cc/ZYsyKGsg/10-10-26-18-27-45-633.png" alt="Screenshot 6" width="400"></td>
  </tr>
  <tr>
    <td><img src="https://i.postimg.cc/9FvRyGh4/10-10-26-18-37-47-426.png" alt="Screenshot 7" width="400"></td>
    <td><img src="https://i.postimg.cc/pLbrmRfF/10-10-26-18-45-48-07.png" alt="Screenshot 8" width="400"></td>
  </tr>
  <tr>
    <td><img src="https://i.postimg.cc/s2fh23yr/10-10-26-18-47-44-358.png" alt="Screenshot 9" width="400"></td>
    <td><img src="https://i.postimg.cc/dtm3Zg5t/10-10-26-18-49-30-756.png" alt="Screenshot 10" width="400"></td>
  </tr>
  <tr>
    <td><img src="https://i.postimg.cc/J4q7zZzd/10-10-26-18-51-13-56.png" alt="Screenshot 11" width="400"></td>
    <td><img src="https://i.postimg.cc/659wgqfj/10-10-26-18-52-28-651.png" alt="Screenshot 12" width="400"></td>
  </tr>
 
</table>

</details>

## Features

| | What to expect |
| :--- | :--- |
| **Native 3DS homebrew** | Runs directly on the console's ARM11 using libctru, Citro2D and Citro3D, without an emulator. |
| **Two screens, one adventure** | The game on top, with a dedicated touch interface below in place of the START menu. |
| **Four languages** | English, Spanish, French and Italian, each built from your own cartridge of that language: texts, graphics and credits come from your ROM. |
| **Optional voxel overworld** | Modelled buildings, trees, signposts and terrain relief, with adjustable camera angle and zoom, and real stereoscopic 3D on a New 3DS. |
| **HD battle interface** | Info boxes and text box drawn at the top screen's full resolution; optional 3D battles over the voxel world. |
| **Follower Pokémon** | Optional: your lead Pokémon walks behind you with its HeartGold/SoulSilver overworld sprite and answers when you talk to it. |
| **Optional day/night lighting** | Morning, daylight, sunset and night outdoors in 2D and voxel mode, lit windows and street lamps, and a clock that can run up to 120X. |
| **Local wireless play** *(experimental)* | Union Room, trades, battles, Berry Blender, minigames and link contests between 3DS systems nearby. |
| **Enhancements** | All optional: physical/special split, IVs and EVs on the summary, infinite TMs, running indoors, Repel prompt, visible wild Pokémon, faster speeds and more. |
| **Fairy type** | This fork adds Gen 6's Fairy type, the 18 species retcons and seven Gen 6 Fairy moves, using official Gen 6 learnsets. |
| **Built from your own cartridge** | The builder generates the game data locally from your own dump. No ROM content is distributed. |

### A new perspective on Hoenn

The voxel overworld is **off by default**. Open **OPTION** on the bottom
screen and enable **VOXEL 3D**, then adjust **3D ANGLE** and **3D ZOOM** to
set your camera. On a New 3DS, raise the 3D slider for a stereoscopic world;
**3D WORLD** and **3D DEPTH** (OPTION → SETTINGS, second page) control it.

> **3D mode is a work in progress.** Many towns and routes now have modelled
> buildings and relief, but large parts of the map and most interiors are
> still shown flat, and the Battle Frontier is only an early start. More
> areas will be modelled as the project moves forward.

### Day and night

In **OPTION → ENHANCEMENTS**, set **DAY / NIGHT** to **AUTO** to enable
outdoor lighting inspired by HeartGold/SoulSilver. It is **OFF by default**;
indoors, caves, underwater areas, menus and classic battles keep their
original colours. Nights have a soft moonlit blue, and supported voxel
windows and street lamps glow warm.

**CLOCK SPEED** selects **1X, 6X, 12X, 24X, 60X or 120X**. At 1X, lighting
follows Emerald's own clock; higher speeds advance a separate clock (60X is
a day in 24 real minutes) and berries grow with it. Daily events and the
GBA save format stay original, and time with the console asleep or off runs
at 1X. Back up `emerald3ds.clock` and `emerald3ds.clock.bak` together with
`emerald3ds.sav`.

**WILD POKEMON → TIMED** changes some grass encounters by morning, day and
night on routes 101–104, 110, 116–117, 119–121 and 123 (**ORIGINAL**, the
default, keeps the original tables). **SHOW CLOCK → ON** adds the time to the
bottom screen's map. More in the [day/night guide](docs/DAY_NIGHT.md).

### Follower Pokémon and local wireless

**OPTION → ENHANCEMENTS → FOLLOWER** makes your lead Pokémon walk behind you.
Its sprites and messages come from HeartGold/SoulSilver: the builder
downloads them while it builds (the only step that needs an Internet
connection; without one, the game is built without them).

**Local wireless play is experimental**: two to four consoles with the same
version and language can meet in the Union Room and use the link features of
Pokémon Centers, the Berry Blender, contests and the Battle Tower. Expect
bugs, and back up your save before trying it.

## Getting started

### Recommended: the universal builder

1. Download `Emerald3DS-Fairy-Builder-universal.zip` from the [latest release of this fork](https://github.com/klx1204/emerald-3ds-fairy/releases/latest) and extract the whole ZIP.
2. Install **Python 3.11 or newer** with Pillow, in a virtual environment next to the launchers:
   ```sh
   python3 -m venv .venv
   .venv/bin/pip install -r requirements.txt      # Windows: .venv\Scripts\pip install -r requirements.txt
   ```
   The launchers use `.venv` automatically when it exists.
3. Start the builder:
   - Windows: double-click `run-builder.bat`
   - macOS: `./run-builder.command` (or double-click it)
   - Linux: `./run-builder.sh`
4. Choose your clean English Emerald ROM and your SD card, then press **Install**.
5. Complete the **sound setup** described in the [installation guide](docs/INSTALLATION.md) before launching the game.

The same ZIP works on every system: it holds the builder source, the engine-only 3DSX and the data recipe, and the game data is generated on your own computer from your own clean ROM. Nothing is uploaded, and your ROM is only read, not copied or modified.

The window needs Tk, which the python.org and Homebrew builds include; on Linux install `python3-tk`. Without Tk the command line still works:

```sh
./run-builder.sh build --rom /path/to/rom.gba --output out
./run-builder.sh install --rom /path/to/rom.gba --sd /path/to/card
```

The builder writes `/3ds/emerald3ds/Emerald3DS.3dsx`, `Emerald3DS.smdh` and `emerald3ds.pak`. It needs an Internet connection only to download the optional follower sprites.

See the [builder documentation](builder/) for additional commands, and the [installation guide](docs/INSTALLATION.md) for updates.

### Supported cartridges

This fork is **English-only**: it accepts the English cartridge and nothing else. Only clean, unmodified dumps are accepted.

| Language | Cartridge | Game code |
| :--- | :--- | :--- |
| English | Pokémon Emerald Version (USA, Europe) | BPEE |

The Spanish, French and Italian builds of the upstream project are not part of this fork, and other languages (German, Japanese) and ROM hacks are not supported.

### Updating or having trouble?

**The [upstream website](https://emerald-3ds.com/) and the [installation guide](docs/INSTALLATION.md) cover the console setup, sound and updates; that site's web builder produces the vanilla game, not this fork.**

- **No sound?** Follow the sound setup instructions; the required DSP firmware file is separate from the generated game files.
- **Using an emulator?** Follow the emulator instructions and use its emulated SD card location.
- **Missing or incompatible data pack?** Generate the pack again with the builder from the same release as the 3DSX.
- **Still stuck?** Open an issue on [this fork](https://github.com/klx1204/emerald-3ds-fairy/issues); the upstream Discord and issue tracker are for the vanilla project.

## About this repository

**This repository contains no game content.** It holds the port's own code,
the tools that build it and the builder that turns *your own* cartridge dump
into the game's data pack. Nothing derived from the ROM is distributed here or
in the releases.

| Component | Location | Role |
| :--- | :--- | :--- |
| Engine | [pret/pokeemerald](https://github.com/pret/pokeemerald) · [`upstream.lock`](upstream.lock) | The Pokémon Emerald decompilation, pinned to a specific revision. |
| Port patches | [`patches/pokeemerald/`](patches/pokeemerald) | The port's changes to the upstream engine. |
| 3DS backend | [`3ds_port/`](3ds_port) | ARM11 backend, GPU compositor, NDSP audio, touch UI and voxel overworld. |
| Data builder | [`builder/`](builder/) | Creates the data pack locally from the player's own supported ROM. |

## Building from source

```sh
python tools/bootstrap.py        # pinned upstream + patches + port -> build/upstream
python tools/bootstrap.py --make # also builds the 3DSX there
python tools/bootstrap.py --make --spanish-rom esmeralda.gba  # Spanish build
python tools/bootstrap.py --make --french-rom emeraude.gba    # French build
python tools/bootstrap.py --make --italian-rom smeraldo.gba   # Italian build
```

The Spanish, French and Italian builds take their texts and graphics from your own
clean Spanish (BPES), French (BPEF) or Italian (BPEI) ROM; see
[Pokémon Esmeralda en español](docs/SPANISH.md),
[Pokémon Émeraude en français](docs/FRENCH.md) and
[Pokémon Smeraldo in italiano](docs/ITALIAN.md).

Start with the [development guide](docs/DEVELOPMENT.md) for requirements,
the development loop, loose data, data packs and host tests.

## Documentation

**For players: [emerald-3ds.com](https://emerald-3ds.com/) brings together the web builder, complete instructions and FAQ.** The repository guides below provide additional reference and development documentation.

| Guide | What's inside |
| :--- | :--- |
| [Install and update](docs/INSTALLATION.md) | Installation, sound setup and updating an existing installation. |
| [Development](docs/DEVELOPMENT.md) | Build requirements, workflow and tests. |
| [Spanish build](docs/SPANISH.md) | Playing in Spanish with your own Pokémon Esmeralda (Spain) ROM. |
| [French build](docs/FRENCH.md) | Playing in French with your own Pokémon Émeraude (France) ROM. |
| [Italian build](docs/ITALIAN.md) | Playing in Italian with your own Pokémon Versione Smeraldo (Italy) ROM. |
| [Architecture](docs/ARCHITECTURE.md) | How the engine and the 3DS backend fit together. |
| [Asset pipeline](docs/ASSET_PIPELINE.md) | How game data is prepared for the port. |
| [Releasing](docs/RELEASING.md) | Building and packaging a release. |
| [Contributing](CONTRIBUTING.md) | Guidelines for contributing to the project. |
| [Changelog](CHANGELOG.md) | Changes across releases. |

## Community

Before asking for installation or update help, please check the **[website instructions and FAQ](https://emerald-3ds.com/)**.

Join the **[Discord community](https://discord.com/invite/tfqHF8496P)** to
talk about the project and share your adventures in Hoenn. Follow
**[@DustZallax on X](https://x.com/DustZallax)** for project updates and
to stay in touch.

<p align="center">
  <a href="https://discord.com/invite/tfqHF8496P"><img src="https://img.shields.io/badge/Join_us_on-Discord-5865F2?style=for-the-badge&amp;logo=discord&amp;logoColor=white" alt="Join us on Discord"></a>
</p>

## Support the project

This fork is **non-commercial**. Because it includes an asset adapted from
CFRU, it does not accept donations. If you would like to support the
upstream project, see [ZallaxDev/emerald-3ds](https://github.com/ZallaxDev/emerald-3ds).

You can support this fork by starring the repository, sharing it or
[contributing](CONTRIBUTING.md).

---

## Provenance and licences

Only original Emerald 3DS code, tools and documentation are licensed by this
project ([LICENSE-PORT.md](LICENSE-PORT.md)). The decompilation, the game and
third-party components keep their own terms; see [NOTICE.md](NOTICE.md) and
[docs/PROVENANCE.md](docs/PROVENANCE.md). AI-assisted tooling was used during
development: [AI_DISCLOSURE.md](AI_DISCLOSURE.md).

Emerald 3DS is an unofficial fan project, not affiliated with or endorsed by
Nintendo, Game Freak, Creatures or The Pokémon Company. Pokémon and Pokémon
Emerald are trademarks of their respective owners.
