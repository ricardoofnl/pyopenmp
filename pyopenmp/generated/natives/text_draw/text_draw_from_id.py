import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_FromID", ctypes.c_void_p, [ctypes.c_int])


def text_draw_from_id(textdrawid):
    return _fn(textdrawid)
