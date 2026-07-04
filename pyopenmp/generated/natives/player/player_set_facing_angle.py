import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetFacingAngle", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float])


def player_set_facing_angle(player, angle):
    return _fn(player, angle)
