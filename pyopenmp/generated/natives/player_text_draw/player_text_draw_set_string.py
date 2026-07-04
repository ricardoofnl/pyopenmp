import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextDraw_SetString", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p])


def player_text_draw_set_string(player, textdraw, text):
    return _fn(player, textdraw, _capi.enc(text))
