import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_HideForAll", ctypes.c_bool, [ctypes.c_void_p])


def text_draw_hide_for_all(textdraw):
    return _fn(textdraw)
