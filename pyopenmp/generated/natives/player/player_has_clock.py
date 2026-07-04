import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_HasClock", ctypes.c_bool, [ctypes.c_void_p])


def player_has_clock(player):
    return _fn(player)
