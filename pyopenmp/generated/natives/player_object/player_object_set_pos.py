import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerObject_SetPos", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def player_object_set_pos(player, object, x, y, z):
    return _fn(player, object, x, y, z)
