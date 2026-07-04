import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextLabel_GetDrawDistance", ctypes.c_float, [ctypes.c_void_p])


def text_label_get_draw_distance(textlabel):
    return _fn(textlabel)
