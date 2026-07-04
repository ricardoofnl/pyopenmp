import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetGravity", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float])


def player_set_gravity(player, gravity):
    return _fn(player, gravity)
