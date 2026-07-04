import ctypes
import importlib
import os
import sys
import traceback

from pyopenmp import _capi

_COMPONENT_UID = 0x70796F70656E6D70

_state = {}


def _log(message):
    print("[pyopenmp] " + message, file=sys.stderr, flush=True)


def start():
    _log("start")
    _capi.load()
    _log("capi loaded")
    component = _register_component()
    _log("component registered")
    return component


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

    _log("calling Component_Create")
    component = create(
        _COMPONENT_UID,
        b"pyopenmp",
        _capi.ComponentVersion(0, 1, 0, 0),
        ctypes.cast(on_ready, ctypes.c_void_p),
        ctypes.cast(on_reset, ctypes.c_void_p),
        ctypes.cast(on_free, ctypes.c_void_p),
    )
    _log("Component_Create returned")
    return component


def _on_ready():
    _log("on_ready")
    try:
        from pyopenmp.generated import events

        events.register_all()
        _log("events registered")
        _load_gamemode()
        _log("gamemode loaded")
    except Exception:
        traceback.print_exc()


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
