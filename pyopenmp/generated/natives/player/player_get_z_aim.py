import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetZAim", ctypes.c_float, [ctypes.c_void_p])


def player_get_z_aim(player):
    return _fn(player)
