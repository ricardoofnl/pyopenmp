import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_BeginEditing", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def object_begin_editing(player, object):
    return _fn(player, object)
