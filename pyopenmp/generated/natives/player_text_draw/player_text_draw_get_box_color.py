import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextDraw_GetBoxColor", ctypes.c_int, [ctypes.c_void_p, ctypes.c_void_p])


def player_text_draw_get_box_color(player, textdraw):
    return _fn(player, textdraw)
