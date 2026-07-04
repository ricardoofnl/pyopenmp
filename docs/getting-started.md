# Getting started

## 1. Prerequisites

- **32-bit Python 3.x** (open.mp is 32-bit, so the embedded interpreter must be too).
- An **open.mp server** (download from [open.mp](https://open.mp)); it already ships
  the `$CAPI` component that pyopenmp calls into.
- **CMake** and a **C compiler**, only if you build the native component yourself
  (option B below).

## 2. Write a gamemode

Your gamemode is a Python package in a `gamemodes/` folder at the server root
(next to `components/`, not inside it). Its `gamemodes/__init__.py` is the entry
point. It is imported once on startup.

`gamemodes/__init__.py`:

```python
from pyopenmp import Player, colors, on_player_connect, on_player_command_text

from gamemodes.core import core


@on_player_connect
def welcome(player: Player):
    player.send_client_message(colors.GREEN, "Welcome!")


@on_player_command_text
def commands(player: Player, text: str) -> bool:
    return core.handle_command(player, text)
```

Every event has a decorator named after it (`on_player_connect`,
`on_player_spawn`, ...). Entities are classes with methods:
`player.set_health(100.0)`, `player.get_pos()` (returns `(x, y, z)` or `None`).
Functions not tied to an entity live in `pyopenmp.generated.natives`
(e.g. `core_log("hi")`).

### Splitting the gamemode into multiple files

Only `gamemodes/__init__.py` is imported automatically, not every `.py` file in
the folder. Other modules run when something imports them, so import them from
`__init__.py` (directly or indirectly) to activate their handlers. A handler in
a file nobody imports never fires.

Import other files as normal Python modules under the `gamemodes` package. For
`gamemodes/core/core.py`, use `from gamemodes.core import core` or
`from gamemodes.core.core import handle_command`. Each subfolder needs an
`__init__.py` (it can be empty). Relative imports work too, e.g.
`from .core import core` inside `gamemodes/__init__.py`.

## 3. Get the runtime (a `components/` folder)

### Option A: download a prebuilt release (recommended)

Grab the latest `pyopenmp-<version>.zip` from the
[latest release](https://github.com/ricardoofnl/pyopenmp/releases/latest). It
already contains a ready `components/` folder with `pyopenmp_native.so`,
`pyopenmp_native.dll`, and the `pyopenmp/` runtime package. Unzip it and copy
that folder's contents straight into your server's `components/`:

```sh
gh release download --repo ricardoofnl/pyopenmp --pattern 'pyopenmp-*.zip'
unzip pyopenmp-*.zip
cp -r components/* /path/to/server/Server/components/
```

No GitHub CLI? Download the zip from the releases page in your browser and copy
the unzipped `components/` files into `Server/components/` the same way.

Pick the release whose Python version matches your 32-bit Python (or run the
**Release** workflow with your own `python_version`).

### Option B: build it yourself

The one native piece embeds CPython. Build it once (see
[`testing.md`](testing.md) for the 32-bit details):

```sh
cmake -S native -B native/build
cmake --build native/build
```

This produces `pyopenmp_native.so` (Linux) / `pyopenmp_native.dll` (Windows).
Put it, plus the `pyopenmp/` runtime package from this repo, into your server's
`components/` folder.

## 4. Deploy your gamemode

The `components/` folder (from step 3) already holds `pyopenmp_native.so` and the
`pyopenmp/` runtime package. Now put your `gamemodes/` package at the server
root, next to `components/`. (The `$CAPI` component is already shipped by the
server.)

The component puts both the server root and `components/` on `sys.path`, so this
works no matter which directory the server is launched from (including runners
like `sampctl`).

## 5. Run

```sh
cd /path/to/server/Server
./omp-server
```

On startup the component boots Python and imports the `gamemodes` package.
Connect a client and you should see the welcome message.

Set `PYOPENMP_GAMEMODE` to import a different package/module name (default
`gamemodes`).

## Coverage

Every wrapped native and event is listed in [`GENERATED.md`](../GENERATED.md).
Regenerate the bindings with `python tools/codegen.py`.
