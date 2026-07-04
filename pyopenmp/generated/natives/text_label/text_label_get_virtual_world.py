import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextLabel_GetVirtualWorld", ctypes.c_int, [ctypes.c_void_p])


def text_label_get_virtual_world(textlabel):
    return _fn(textlabel)
