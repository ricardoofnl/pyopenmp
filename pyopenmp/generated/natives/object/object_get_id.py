import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_GetID", ctypes.c_int, [ctypes.c_void_p])


def object_get_id(object):
    return _fn(object)
