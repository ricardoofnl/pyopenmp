# Getting started

## 1. Prerequisites

- **32-bit Python 3.x** (open.mp is 32-bit, so the embedded interpreter must be too).
- **CMake** and a **C compiler** (to build the native component once).
- An **open.mp server** (download from [open.mp](https://open.mp)); it already ships
  the `$CAPI` component that pyopenmp calls into.

## 2. Write a gamemode

Create `gamemode.py`:

```python
from pyopenmp import Player, colors, on_player_connect, on_player_command_text


@on_player_connect
def welcome(player: Player):
    player.send_client_message(colors.GREEN, "Welcome!")


@on_player_command_text
def commands(player: Player, text: str) -> bool:
    if text == "/help":
        player.send_client_message(colors.YELLOW, "Commands: /help")
        return True
    return False
```

Every event has a decorator named after it (`on_player_connect`,
`on_player_spawn`, ...). Entities are classes with methods:
`player.set_health(100.0)`, `player.get_pos()` (returns `(x, y, z)` or `None`).
Functions not tied to an entity live in `pyopenmp.generated.natives`
(e.g. `core_log("hi")`).

## 3. Build the native component

The one native piece embeds CPython. Build it once (see
[`testing.md`](testing.md) for the 32-bit details):

```sh
cmake -S native -B native/build
cmake --build native/build
```

This produces `pyopenmp.so` (Linux) / `pyopenmp.dll` (Windows).

## 4. Deploy

Into your server:

- `pyopenmp.so` → `Server/components/`
- the `pyopenmp/` package folder → server root (so it is importable)
- your `gamemode.py` → server root

## 5. Run

```sh
cd /path/to/server/Server
./omp-server
```

On startup the component boots Python and loads your gamemode. Connect a client
and you should see the welcome message.

Set `PYOPENMP_GAMEMODE` to import a different module name (default `gamemode`).

## Coverage

Every wrapped native and event is listed in [`GENERATED.md`](../GENERATED.md).
Regenerate the bindings with `python tools/codegen.py`.
