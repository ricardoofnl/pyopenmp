import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetTeam", ctypes.c_int, [ctypes.c_void_p])


def player_get_team(player):
    return _fn(player)
