import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetSurfingPlayerObject", ctypes.c_void_p, [ctypes.c_void_p])


def player_get_surfing_player_object(player):
    return _fn(player)
