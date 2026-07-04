import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetDistanceFromPoint", ctypes.c_float, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def player_get_distance_from_point(player, x, y, z):
    return _fn(player, x, y, z)
