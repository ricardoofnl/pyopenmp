import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Pickup_GetType", ctypes.c_int, [ctypes.c_void_p])


def pickup_get_type(pickup):
    return _fn(pickup)
