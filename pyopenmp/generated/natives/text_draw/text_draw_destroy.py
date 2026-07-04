import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_Destroy", ctypes.c_bool, [ctypes.c_void_p])


def text_draw_destroy(textdraw):
    return _fn(textdraw)
