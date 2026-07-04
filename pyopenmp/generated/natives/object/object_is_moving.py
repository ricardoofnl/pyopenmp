import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_IsMoving", ctypes.c_bool, [ctypes.c_void_p])


def object_is_moving(object):
    return _fn(object)
