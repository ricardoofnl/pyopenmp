import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextLabel_UpdateText", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_char_p])


def player_text_label_update_text(player, textlabel, color, text):
    return _fn(player, textlabel, color, _capi.enc(text))
