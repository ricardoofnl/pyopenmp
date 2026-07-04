import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetArmor", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float])


def player_set_armor(player, armor):
    return _fn(player, armor)
