import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_Kick", ctypes.c_bool, [ctypes.c_void_p])


def player_kick(player):
    return _fn(player)
