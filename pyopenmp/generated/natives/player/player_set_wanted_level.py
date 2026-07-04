import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetWantedLevel", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def player_set_wanted_level(player, level):
    return _fn(player, level)
