import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetPosFindZ", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def player_set_pos_find_z(player, x, y, z):
    return _fn(player, x, y, z)
