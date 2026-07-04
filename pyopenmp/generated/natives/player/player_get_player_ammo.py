import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetPlayerAmmo", ctypes.c_int, [ctypes.c_void_p])


def player_get_player_ammo(player):
    return _fn(player)
