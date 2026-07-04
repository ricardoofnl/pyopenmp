# Getting started

## 1. Prerequisites

- **32-bit Python 3.x** (open.mp is 32-bit, so the embedded interpreter must be too).
- **CMake** and a **C compiler** (to build the native component once).
- An **open.mp server** (download from [open.mp](https://open.mp)); it already ships
  the `$CAPI` component that pyopenmp calls into.

## 2. Write a gamemode

Your gamemode is a Python package in a `gamemodes/` folder at the server root
(next to `components/`, not inside it). Its `gamemodes/__init__.py` is the entry
point — it is imported once on startup.

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

## 3. Build the native component

The one native piece embeds CPython. Build it once (see
[`testing.md`](testing.md) for the 32-bit details):

```sh
cmake -S native -B native/build
cmake --build native/build
```

This produces `pyopenmp_native.so` (Linux) / `pyopenmp_native.dll` (Windows).

## 4. Deploy

Put `pyopenmp_native.so` and the `pyopenmp/` runtime package inside the server's
`components/` folder. Put your `gamemodes/` package at the server root, next to
`components/`. (The `$CAPI` component is already shipped by the server.)

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
