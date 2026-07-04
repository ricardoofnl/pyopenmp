import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Pickup_Create", ctypes.c_void_p, [ctypes.c_int, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_int, ctypes.POINTER(ctypes.c_int)])


def pickup_create(model, type, x, y, z, virtual_world):
    id = ctypes.c_int()
    __ret = _fn(model, type, x, y, z, virtual_world, ctypes.byref(id))
    return (__ret, id.value)
