import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_SetStringForPlayer", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p])


def text_draw_set_string_for_player(textdraw, player, text):
    return _fn(textdraw, player, _capi.enc(text))
