import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GiveMoney", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def player_give_money(player, amount):
    return _fn(player, amount)
