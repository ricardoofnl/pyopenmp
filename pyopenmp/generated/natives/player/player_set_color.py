import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetColor", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_uint32])


def player_set_color(player, color):
    return _fn(player, color)
