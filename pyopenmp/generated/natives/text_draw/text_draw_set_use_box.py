import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_SetUseBox", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_bool])


def text_draw_set_use_box(textdraw, use):
    return _fn(textdraw, use)
