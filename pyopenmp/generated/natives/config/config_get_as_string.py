import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Config_GetAsString", ctypes.c_int, [ctypes.c_char_p, ctypes.POINTER(_capi.CAPIStringBuffer)])


def config_get_as_string(cvar):
    output = _capi.OutBuffer()
    __ret = _fn(_capi.enc(cvar), ctypes.byref(output.raw))
    return output.value()
