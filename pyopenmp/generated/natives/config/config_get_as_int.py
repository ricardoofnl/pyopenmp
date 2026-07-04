import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Config_GetAsInt", ctypes.c_int, [ctypes.c_char_p])


def config_get_as_int(cvar):
    return _fn(_capi.enc(cvar))
