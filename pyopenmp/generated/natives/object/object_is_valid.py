import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_IsValid", ctypes.c_bool, [ctypes.c_void_p])


def object_is_valid(object):
    return _fn(object)
