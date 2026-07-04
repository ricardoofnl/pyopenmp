import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetID", ctypes.c_int, [ctypes.c_void_p])


def player_get_id(player):
    return _fn(player)
