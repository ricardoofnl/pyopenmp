import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_GetWeather", ctypes.c_int, [])


def core_get_weather():
    return _fn()
