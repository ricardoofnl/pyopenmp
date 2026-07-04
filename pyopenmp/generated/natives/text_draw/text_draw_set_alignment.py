import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_SetAlignment", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def text_draw_set_alignment(textdraw, alignment):
    return _fn(textdraw, alignment)
