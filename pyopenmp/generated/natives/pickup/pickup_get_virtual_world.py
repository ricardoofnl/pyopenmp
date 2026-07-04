import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Pickup_GetVirtualWorld", ctypes.c_int, [ctypes.c_void_p])


def pickup_get_virtual_world(pickup):
    return _fn(pickup)
