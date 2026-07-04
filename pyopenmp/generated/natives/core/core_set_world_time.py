import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_SetWorldTime", ctypes.c_bool, [ctypes.c_int])


def core_set_world_time(hour):
    return _fn(hour)
