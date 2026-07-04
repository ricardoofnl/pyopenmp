import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_StopAudioStream", ctypes.c_bool, [ctypes.c_void_p])


def player_stop_audio_stream(player):
    return _fn(player)
