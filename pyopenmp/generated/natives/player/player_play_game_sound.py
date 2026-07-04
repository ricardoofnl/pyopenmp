import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_PlayGameSound", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def player_play_game_sound(player, sound, x, y, z):
    return _fn(player, sound, x, y, z)
