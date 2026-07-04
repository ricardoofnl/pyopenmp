import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetWeather", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def player_set_weather(player, weather):
    return _fn(player, weather)
