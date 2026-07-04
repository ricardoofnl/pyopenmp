import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextDraw_SetBoxColor", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32])


def player_text_draw_set_box_color(player, textdraw, color):
    return _fn(player, textdraw, color)
