import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_ShowGameTextForAll", ctypes.c_bool, [ctypes.c_char_p, ctypes.c_int, ctypes.c_int])


def core_show_game_text_for_all(msg, time, style):
    return _fn(_capi.enc(msg), time, style)
