import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SelectTextDraw", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_uint32])


def player_select_text_draw(player, hover_colour):
    return _fn(player, hover_colour)
