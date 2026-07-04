import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_TickCount", ctypes.c_uint32, [])


def core_tick_count():
    return _fn()
