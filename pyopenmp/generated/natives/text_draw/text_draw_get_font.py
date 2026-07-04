import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_GetFont", ctypes.c_int, [ctypes.c_void_p])


def text_draw_get_font(textdraw):
    return _fn(textdraw)
