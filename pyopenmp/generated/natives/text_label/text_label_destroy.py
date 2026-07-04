import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextLabel_Destroy", ctypes.c_bool, [ctypes.c_void_p])


def text_label_destroy(textlabel):
    return _fn(textlabel)
