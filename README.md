# pyopenmp

Write [open.mp](https://open.mp) gamemodes in **Python**.

pyopenmp brings Python scripting to open.mp, in the spirit of
[PySAMP](https://github.com/pysamp/PySAMP). A tiny native component embeds
CPython; everything else is pure Python that calls the open.mp C-API (`$CAPI`,
shipped with the server) directly through `ctypes`. The whole native surface
(772 functions, 91 events) is generated from the C-API specs.

```python
from pyopenmp import on_player_connect, on_player_command_text, colors, Player


@on_player_connect
def welcome(player: Player):
    player.send_client_message(colors.GREEN, "Welcome to the server!")


@on_player_command_text
def commands(player: Player, text: str) -> bool:
    if text == "/help":
        player.send_client_message(colors.YELLOW, "Commands: /help")
        return True
    return False
```

## Layout

- `native/`: minimal C component that embeds CPython and starts your gamemode.
- `pyopenmp/`: the Python package you copy to the server: entities, events, colors, and the generated bindings.
- `tools/codegen.py`: generates the ctypes bindings from `api.json` / `events.json`.
- `examples/gamemodes/`: example gamemode package (with a `core/` submodule).
- `third_party/open.mp-capi/`: vendored C-API specs (MPL-2.0).

Every generated native and event is listed in [`GENERATED.md`](GENERATED.md).

## Releases

Download the latest [`pyopenmp-<version>.zip`](https://github.com/ricardoofnl/pyopenmp/releases/latest)
and copy the `components/` files it contains straight into your server's
`components/` folder, no build step needed:

```sh
gh release download --repo ricardoofnl/pyopenmp --pattern 'pyopenmp-*.zip'
unzip pyopenmp-*.zip
cp -r components/* /path/to/server/Server/components/
```

The zip's `components/` holds `pyopenmp_native.so`, `pyopenmp_native.dll`, and the
`pyopenmp/` runtime package. Then add your `gamemodes/` package at the server
root.
## Important: 32-bit Python

open.mp is **32-bit**, so the embedded interpreter and `$CAPI` are 32-bit. Use a
**32-bit Python** build (like PySAMP). See [`docs/testing.md`](docs/testing.md).

## License

Licensed under the [Mozilla Public License 2.0](LICENSE).
