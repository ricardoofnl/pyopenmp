import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_Spawn", ctypes.c_bool, [ctypes.c_void_p])


def player_spawn(player):
    return _fn(player)
