import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_BeginSelecting", ctypes.c_bool, [ctypes.c_void_p])


def object_begin_selecting(player):
    return _fn(player)
