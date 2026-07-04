import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetHealth", ctypes.c_float, [ctypes.c_void_p])


def player_get_health(player):
    return _fn(player)
