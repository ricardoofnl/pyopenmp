import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_GetColor", ctypes.c_int, [ctypes.c_void_p])


def text_draw_get_color(textdraw):
    return _fn(textdraw)
