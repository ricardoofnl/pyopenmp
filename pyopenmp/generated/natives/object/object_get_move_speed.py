import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_GetMoveSpeed", ctypes.c_float, [ctypes.c_void_p])


def object_get_move_speed(object):
    return _fn(object)
