import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextDraw_GetFont", ctypes.c_int, [ctypes.c_void_p, ctypes.c_void_p])


def player_text_draw_get_font(player, textdraw):
    return _fn(player, textdraw)
