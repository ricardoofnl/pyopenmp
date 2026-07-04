import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Config_GetAsFloat", ctypes.c_float, [ctypes.c_char_p])


def config_get_as_float(cvar):
    return _fn(_capi.enc(cvar))
