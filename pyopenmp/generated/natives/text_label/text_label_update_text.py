import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextLabel_UpdateText", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_char_p])


def text_label_update_text(textlabel, color, text):
    return _fn(textlabel, color, _capi.enc(text))
