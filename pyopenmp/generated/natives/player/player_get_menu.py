import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetMenu", ctypes.c_void_p, [ctypes.c_void_p])


def player_get_menu(player):
    return _fn(player)
