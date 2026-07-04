import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Pickup_AddStatic", ctypes.c_bool, [ctypes.c_int, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_int])


def pickup_add_static(model, type, x, y, z, virtual_world):
    return _fn(model, type, x, y, z, virtual_world)
