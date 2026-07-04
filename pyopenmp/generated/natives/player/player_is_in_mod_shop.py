import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_IsInModShop", ctypes.c_bool, [ctypes.c_void_p])


def player_is_in_mod_shop(player):
    return _fn(player)
