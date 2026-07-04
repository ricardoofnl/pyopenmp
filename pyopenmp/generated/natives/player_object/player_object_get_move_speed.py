import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerObject_GetMoveSpeed", ctypes.c_float, [ctypes.c_void_p, ctypes.c_void_p])


def player_object_get_move_speed(player, object):
    return _fn(player, object)
