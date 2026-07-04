import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_IsAdmin", ctypes.c_bool, [ctypes.c_void_p])


def player_is_admin(player):
    return _fn(player)
