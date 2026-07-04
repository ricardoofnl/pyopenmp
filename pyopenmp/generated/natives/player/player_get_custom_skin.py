import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetCustomSkin", ctypes.c_int, [ctypes.c_void_p])


def player_get_custom_skin(player):
    return _fn(player)
