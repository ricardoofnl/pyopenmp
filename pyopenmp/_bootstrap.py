import ctypes
import importlib
import os
import traceback

from pyopenmp import _capi

_COMPONENT_UID = 0x70796F70656E6D70

_state = {}


def start():
    _capi.load()
    _register_component()


def _register_component():
    lib = _capi.load()
    create = lib.Component_Create
    create.restype = ctypes.c_void_p
    create.argtypes = [
        ctypes.c_uint64,
        ctypes.c_char_p,
        _capi.ComponentVersion,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p,
    ]

    cb_type = ctypes.CFUNCTYPE(None)
    on_ready = cb_type(_on_ready)
    on_reset = cb_type(_on_reset)
    on_free = cb_type(_on_free)
    _state["callbacks"] = (on_ready, on_reset, on_free)

    create(
        _COMPONENT_UID,
        b"pyopenmp",
        _capi.ComponentVersion(0, 1, 0, 0),
        ctypes.cast(on_ready, ctypes.c_void_p),
        ctypes.cast(on_reset, ctypes.c_void_p),
        ctypes.cast(on_free, ctypes.c_void_p),
    )


def _on_ready():
    from pyopenmp.generated import events

    events.register_all()
    _load_gamemode()


def _on_reset():
    pass


def _on_free():
    pass


def _load_gamemode():
    module = os.environ.get("PYOPENMP_GAMEMODE", "gamemode")
    try:
        importlib.import_module(module)
    except Exception:
        traceback.print_exc()
