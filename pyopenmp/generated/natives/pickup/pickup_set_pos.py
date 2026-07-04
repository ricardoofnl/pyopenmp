import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Pickup_SetPos", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_bool])


def pickup_set_pos(pickup, x, y, z, update):
    return _fn(pickup, x, y, z, update)
