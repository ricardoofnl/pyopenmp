import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetPlayerSpectateID", ctypes.c_int, [ctypes.c_void_p])


def player_get_player_spectate_id(player):
    return _fn(player)
