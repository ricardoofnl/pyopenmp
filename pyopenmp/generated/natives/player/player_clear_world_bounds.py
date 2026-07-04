import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_ClearWorldBounds", ctypes.c_bool, [ctypes.c_void_p])


def player_clear_world_bounds(player):
    return _fn(player)
