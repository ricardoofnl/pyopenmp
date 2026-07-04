import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_SetPos", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float])


def text_draw_set_pos(textdraw, x, y):
    return _fn(textdraw, x, y)
