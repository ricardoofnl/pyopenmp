import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetDefaultColor", ctypes.c_uint32, [ctypes.c_void_p])


def player_get_default_color(player):
    return _fn(player)
