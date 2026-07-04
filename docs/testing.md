# Building and testing on a server

## Why 32-bit

open.mp runs as **32-bit**, so the CPython the component embeds — and any Python
that `ctypes`-loads `$CAPI` — must also be **32-bit**. Use a 32-bit Python 3.x
build (PySAMP pins 3.10.4 for the same reason).

## Build the native component

Point CMake at your 32-bit Python:

```sh
cmake -S native -B native/build \
  -DPython3_ROOT_DIR=/path/to/python32 \
  -DCMAKE_C_FLAGS=-m32 -DCMAKE_SHARED_LINKER_FLAGS=-m32
cmake --build native/build
```

On Windows, use a 32-bit Python and the Win32 generator:

```powershell
cmake -S native -B native/build -A Win32 -DPython3_ROOT_DIR=C:\Python32
cmake --build native/build --config Release
```

The output is `pyopenmp.so` / `pyopenmp.dll`.

## Deploy

```
Server/
├── components/
│   ├── $CAPI.so         # shipped by the server
│   └── pyopenmp.so      # the native component you built
├── pyopenmp/            # the Python package (copied from this repo)
└── gamemode.py          # your gamemode
```

`pyopenmp/` and `gamemode.py` go in the **server root** (the working directory
`omp-server` runs from), because the component adds that directory to
`sys.path`.

## Run and verify

```sh
cd /path/to/server/Server
./omp-server
```

- Your `on_ready`/first handlers run as the component boots Python.
- Connect a SA-MP `0.3.7` / open.mp client to `127.0.0.1:7777`; on connect you
  should get the welcome message, and `/help` should respond.

## Troubleshooting

- **`ModuleNotFoundError: pyopenmp`** — the `pyopenmp/` folder is not in the
  server root, or the server was not started from its root directory.
- **Interpreter/segfault on load** — architecture mismatch. The component,
  its embedded Python, and `$CAPI` must all be 32-bit.
- **Python cannot find its standard library** — set `PYTHONHOME` to your 32-bit
  Python installation.
