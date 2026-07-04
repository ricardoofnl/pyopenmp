import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("All_CreateExplosion", ctypes.c_bool, [ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_int, ctypes.c_float])


def all_create_explosion(x, y, z, type, radius):
    return _fn(x, y, z, type, radius)
