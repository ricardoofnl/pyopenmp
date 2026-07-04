import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_AddRule", ctypes.c_bool, [ctypes.c_char_p, ctypes.c_char_p])


def core_add_rule(name, value):
    return _fn(_capi.enc(name), _capi.enc(value))
