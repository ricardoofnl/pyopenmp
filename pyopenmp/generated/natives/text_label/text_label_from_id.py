import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextLabel_FromID", ctypes.c_void_p, [ctypes.c_int])


def text_label_from_id(textlabelid):
    return _fn(textlabelid)
