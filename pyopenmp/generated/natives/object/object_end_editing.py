import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_EndEditing", ctypes.c_bool, [ctypes.c_void_p])


def object_end_editing(player):
    return _fn(player)
