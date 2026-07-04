import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_GetID", ctypes.c_int, [ctypes.c_void_p])


def text_draw_get_id(textdraw):
    return _fn(textdraw)
