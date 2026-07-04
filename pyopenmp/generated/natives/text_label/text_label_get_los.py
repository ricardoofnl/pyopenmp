import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextLabel_GetLOS", ctypes.c_bool, [ctypes.c_void_p])


def text_label_get_los(textlabel):
    return _fn(textlabel)
