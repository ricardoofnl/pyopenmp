import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextLabel_SetVirtualWorld", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def text_label_set_virtual_world(textlabel, world):
    return _fn(textlabel, world)
