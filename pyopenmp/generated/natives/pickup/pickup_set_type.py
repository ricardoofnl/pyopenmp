import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Pickup_SetType", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_bool])


def pickup_set_type(pickup, type, update):
    return _fn(pickup, type, update)
