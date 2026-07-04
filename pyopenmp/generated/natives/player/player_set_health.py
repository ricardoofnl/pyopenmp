import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetHealth", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float])


def player_set_health(player, health):
    return _fn(player, health)
