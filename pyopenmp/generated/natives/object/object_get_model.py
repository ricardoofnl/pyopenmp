import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_GetModel", ctypes.c_int, [ctypes.c_void_p])


def object_get_model(object):
    return _fn(object)
