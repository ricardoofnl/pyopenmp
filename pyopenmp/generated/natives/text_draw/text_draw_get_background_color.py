import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_GetBackgroundColor", ctypes.c_int, [ctypes.c_void_p])


def text_draw_get_background_color(textdraw):
    return _fn(textdraw)
