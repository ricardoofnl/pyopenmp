import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_HideGameText", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def player_hide_game_text(player, style):
    return _fn(player, style)
