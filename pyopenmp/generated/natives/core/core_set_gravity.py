import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_SetGravity", ctypes.c_bool, [ctypes.c_float])


def core_set_gravity(gravity):
    return _fn(gravity)
