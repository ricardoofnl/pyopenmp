import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_IsPlayerUsingOfficialClient", ctypes.c_bool, [ctypes.c_void_p])


def player_is_player_using_official_client(player):
    return _fn(player)
