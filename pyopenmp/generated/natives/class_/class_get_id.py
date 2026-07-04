import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Class_GetID", ctypes.c_int, [ctypes.c_void_p])


def class_get_id(cls):
    return _fn(cls)
