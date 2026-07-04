import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetWeather", ctypes.c_int, [ctypes.c_void_p])


def player_get_weather(player):
    return _fn(player)
