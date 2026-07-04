import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_SetWeather", ctypes.c_bool, [ctypes.c_int])


def core_set_weather(weatherid):
    return _fn(weatherid)
