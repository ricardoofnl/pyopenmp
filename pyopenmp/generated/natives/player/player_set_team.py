import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetTeam", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def player_set_team(player, team):
    return _fn(player, team)
