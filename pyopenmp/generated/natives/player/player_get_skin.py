import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetSkin", ctypes.c_int, [ctypes.c_void_p])


def player_get_skin(player):
    return _fn(player)
