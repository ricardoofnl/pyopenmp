import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetFightingStyle", ctypes.c_int, [ctypes.c_void_p])


def player_get_fighting_style(player):
    return _fn(player)
