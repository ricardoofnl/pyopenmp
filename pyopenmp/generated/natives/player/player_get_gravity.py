import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetGravity", ctypes.c_float, [ctypes.c_void_p])


def player_get_gravity(player):
    return _fn(player)
