import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_SetTextSize", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float])


def text_draw_set_text_size(textdraw, size_x, size_y):
    return _fn(textdraw, size_x, size_y)
