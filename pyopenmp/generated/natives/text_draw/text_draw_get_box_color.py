import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_GetBoxColor", ctypes.c_int, [ctypes.c_void_p])


def text_draw_get_box_color(textdraw):
    return _fn(textdraw)
