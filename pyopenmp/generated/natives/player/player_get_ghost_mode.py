import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetGhostMode", ctypes.c_bool, [ctypes.c_void_p])


def player_get_ghost_mode(player):
    return _fn(player)
