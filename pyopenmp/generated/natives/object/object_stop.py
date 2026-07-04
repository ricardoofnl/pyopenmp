import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_Stop", ctypes.c_bool, [ctypes.c_void_p])


def object_stop(object):
    return _fn(object)
