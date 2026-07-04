import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_SetOutline", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def text_draw_set_outline(textdraw, size):
    return _fn(textdraw, size)
