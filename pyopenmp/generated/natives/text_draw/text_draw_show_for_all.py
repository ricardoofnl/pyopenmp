import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_ShowForAll", ctypes.c_bool, [ctypes.c_void_p])


def text_draw_show_for_all(textdraw):
    return _fn(textdraw)
