import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_ShowGameText", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_int])


def player_show_game_text(player, text, time, style):
    return _fn(player, _capi.enc(text), time, style)
