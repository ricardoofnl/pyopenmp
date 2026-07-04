import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Pickup_Destroy", ctypes.c_bool, [ctypes.c_void_p])


def pickup_destroy(pickup):
    return _fn(pickup)
