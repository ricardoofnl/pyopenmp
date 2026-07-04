import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextLabel_IsStreamedIn", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def text_label_is_streamed_in(player, textlabel):
    return _fn(player, textlabel)
