import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextLabel_SetLOS", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_bool])


def text_label_set_los(textlabel, status):
    return _fn(textlabel, status)
