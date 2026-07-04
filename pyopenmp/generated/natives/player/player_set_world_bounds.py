import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetWorldBounds", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def player_set_world_bounds(player, x_max, x_min, y_max, y_min):
    return _fn(player, x_max, x_min, y_max, y_min)
