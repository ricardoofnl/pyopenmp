import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_SetString", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_char_p])


def text_draw_set_string(textdraw, text):
    return _fn(textdraw, _capi.enc(text))
