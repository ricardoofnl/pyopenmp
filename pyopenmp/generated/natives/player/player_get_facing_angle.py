import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetFacingAngle", ctypes.c_float, [ctypes.c_void_p])


def player_get_facing_angle(player):
    return _fn(player)
