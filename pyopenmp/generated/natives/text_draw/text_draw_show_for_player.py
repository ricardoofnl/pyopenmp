import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_ShowForPlayer", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def text_draw_show_for_player(player, textdraw):
    return _fn(player, textdraw)
