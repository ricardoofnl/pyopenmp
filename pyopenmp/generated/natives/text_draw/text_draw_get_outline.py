import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_GetOutline", ctypes.c_int, [ctypes.c_void_p])


def text_draw_get_outline(textdraw):
    return _fn(textdraw)
