import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextLabel_IsValid", ctypes.c_bool, [ctypes.c_void_p])


def text_label_is_valid(textlabel):
    return _fn(textlabel)
