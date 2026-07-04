# Building and testing on a server

## Why 32-bit

open.mp runs as **32-bit**, so the CPython the component embeds — and any Python
that `ctypes`-loads `$CAPI` — must also be **32-bit**. Use a 32-bit Python 3.x
build (PySAMP pins 3.10.4 for the same reason).

## Build the native component

### Quick build (Linux, gcc)

With a 32-bit Python installed (Fedora: `sudo dnf install python3-devel.i686`;
Debian/Ubuntu: a 32-bit Python build), run:

```sh
./native/build.sh          # -> dist/components/pyopenmp_native.so (32-bit)
```

`PYVER` selects the Python version (defaults to the running one), e.g.
`PYVER=3.10 ./native/build.sh`.

### CMake (cross-platform)

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

The output is `pyopenmp_native.so` / `pyopenmp_native.dll`.

## Deploy

```
Server/
└── components/
    ├── $CAPI.so         (shipped by the server)
    ├── pyopenmp_native.so      (the native component you built)
    ├── pyopenmp/        (the Python package from this repo)
    └── gamemode.py      (your gamemode)
```

Keep `pyopenmp/` and `gamemode.py` **inside `components/`**, next to
`pyopenmp_native.so`. The component adds its own directory to `sys.path`, so this works
regardless of which directory the server is launched from (including runners
like `sampctl`).

## Run and verify

```sh
cd /path/to/server/Server
./omp-server
```

- Your `on_ready`/first handlers run as the component boots Python.
- Connect a SA-MP `0.3.7` / open.mp client to `127.0.0.1:7777`; on connect you
  should get the welcome message, and `/help` should respond.

## Troubleshooting

- **`ModuleNotFoundError: pyopenmp` / `pyopenmp._bootstrap`** — the `pyopenmp/`
  folder (and `gamemode.py`) must sit next to `pyopenmp_native.so` inside `components/`.
- **`undefined symbol: PyExc_...` when importing `ctypes`** — Python extension
  modules could not resolve libpython. The component loads libpython with
  `RTLD_GLOBAL` to avoid this; make sure you are running the latest `pyopenmp_native.so`.
- **Interpreter/segfault on load** — architecture mismatch. The component,
  its embedded Python, and `$CAPI` must all be 32-bit.
- **Python cannot find its standard library** — set `PYTHONHOME` to your 32-bit
  Python installation.
