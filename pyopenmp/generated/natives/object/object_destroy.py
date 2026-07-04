import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_Destroy", ctypes.c_bool, [ctypes.c_void_p])


def object_destroy(object):
    return _fn(object)
