import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Pickup_SetVirtualWorld", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def pickup_set_virtual_world(pickup, virtualworld):
    return _fn(pickup, virtualworld)
