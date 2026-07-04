import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_HasGameText", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def player_has_game_text(player, style):
    return _fn(player, style)
