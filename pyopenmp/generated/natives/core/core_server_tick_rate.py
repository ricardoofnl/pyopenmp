import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_ServerTickRate", ctypes.c_int, [])


def core_server_tick_rate():
    return _fn()
