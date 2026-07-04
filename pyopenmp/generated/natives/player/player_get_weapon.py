import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetWeapon", ctypes.c_int, [ctypes.c_void_p])


def player_get_weapon(player):
    return _fn(player)
