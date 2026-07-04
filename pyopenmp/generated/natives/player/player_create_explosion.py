import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_CreateExplosion", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_int, ctypes.c_float])


def player_create_explosion(player, x, y, z, type, radius):
    return _fn(player, x, y, z, type, radius)
