import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_PlayAudioStream", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_bool])


def player_play_audio_stream(player, url, x, y, z, distance, use_pos):
    return _fn(player, _capi.enc(url), x, y, z, distance, use_pos)
