import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_EnableStuntBonus", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_bool])


def player_enable_stunt_bonus(player, enable):
    return _fn(player, enable)
