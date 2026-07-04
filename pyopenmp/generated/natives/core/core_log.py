import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_Log", ctypes.c_bool, [ctypes.c_char_p])


def core_log(text):
    return _fn(_capi.enc(text))
