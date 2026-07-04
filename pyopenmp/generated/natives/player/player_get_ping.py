import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetPing", ctypes.c_int, [ctypes.c_void_p])


def player_get_ping(player):
    return _fn(player)
