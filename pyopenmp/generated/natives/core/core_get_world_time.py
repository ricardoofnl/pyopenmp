import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_GetWorldTime", ctypes.c_int, [])


def core_get_world_time():
    return _fn()
