import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetFightingStyle", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def player_set_fighting_style(player, style):
    return _fn(player, style)
