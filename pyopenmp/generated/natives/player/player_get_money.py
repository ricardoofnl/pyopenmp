import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetMoney", ctypes.c_int, [ctypes.c_void_p])


def player_get_money(player):
    return _fn(player)
