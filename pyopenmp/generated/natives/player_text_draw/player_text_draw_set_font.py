import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextDraw_SetFont", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int])


def player_text_draw_set_font(player, textdraw, font):
    return _fn(player, textdraw, font)
