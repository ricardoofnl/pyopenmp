import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_IsBox", ctypes.c_bool, [ctypes.c_void_p])


def text_draw_is_box(textdraw):
    return _fn(textdraw)
