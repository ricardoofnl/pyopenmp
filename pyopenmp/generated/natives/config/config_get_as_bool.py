import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Config_GetAsBool", ctypes.c_bool, [ctypes.c_char_p])


def config_get_as_bool(cvar):
    return _fn(_capi.enc(cvar))
