import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextLabel_GetColor", ctypes.c_uint32, [ctypes.c_void_p])


def text_label_get_color(textlabel):
    return _fn(textlabel)
