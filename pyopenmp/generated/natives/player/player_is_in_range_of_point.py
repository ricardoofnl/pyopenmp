import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_IsInRangeOfPoint", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def player_is_in_range_of_point(player, range, x, y, z):
    return _fn(player, range, x, y, z)
