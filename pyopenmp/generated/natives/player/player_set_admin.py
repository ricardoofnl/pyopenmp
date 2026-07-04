import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetAdmin", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_bool])


def player_set_admin(player, set):
    return _fn(player, set)
