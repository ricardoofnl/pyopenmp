import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_GetGravity", ctypes.c_float, [])


def core_get_gravity():
    return _fn()
