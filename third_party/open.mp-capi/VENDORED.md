# Vendored: open.mp C-API

Copied from [`openmultiplayer/open.mp-capi`](https://github.com/openmultiplayer/open.mp-capi),
licensed under **MPL-2.0** (see `LICENSE.md`).

- `apidocs/api.json`: machine-readable spec of all native functions. Consumed by `tools/codegen.py`.
- `apidocs/events.json`: machine-readable spec of all events. Consumed by `tools/codegen.py`.
- `include/ompcapi.h`: reference header (struct/typedef definitions mirrored by the ctypes layer).

The provider component (`$CAPI.so` / `$CAPI.dll`) is shipped by the open.mp server
itself; pyopenmp only calls into it via `ctypes`.
