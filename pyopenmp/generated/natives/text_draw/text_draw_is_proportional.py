import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_IsProportional", ctypes.c_bool, [ctypes.c_void_p])


def text_draw_is_proportional(textdraw):
    return _fn(textdraw)
