import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Actor_Create", ctypes.c_void_p, [ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.POINTER(ctypes.c_int)])


def actor_create(model, x, y, z, rot):
    id = ctypes.c_int()
    __ret = _fn(model, x, y, z, rot, ctypes.byref(id))
    return (__ret, id.value)
