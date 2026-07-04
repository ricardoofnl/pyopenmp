import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_RemoveRule", ctypes.c_bool, [ctypes.c_char_p])


def core_remove_rule(name):
    return _fn(_capi.enc(name))
