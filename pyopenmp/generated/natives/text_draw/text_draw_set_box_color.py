import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_SetBoxColor", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_uint32])


def text_draw_set_box_color(textdraw, color):
    return _fn(textdraw, color)
