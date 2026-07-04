import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Pickup_IsValid", ctypes.c_bool, [ctypes.c_void_p])


def pickup_is_valid(pickup):
    return _fn(pickup)
