import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_SetPos", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def object_set_pos(object, x, y, z):
    return _fn(object, x, y, z)
