import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetArmor", ctypes.c_float, [ctypes.c_void_p])


def player_get_armor(player):
    return _fn(player)
