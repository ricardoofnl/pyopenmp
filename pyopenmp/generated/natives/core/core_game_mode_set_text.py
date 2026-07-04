import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_GameMode_SetText", ctypes.c_bool, [ctypes.c_char_p])


def core_game_mode_set_text(string):
    return _fn(_capi.enc(string))
