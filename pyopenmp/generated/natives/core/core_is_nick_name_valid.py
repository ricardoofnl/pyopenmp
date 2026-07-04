import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_IsNickNameValid", ctypes.c_bool, [ctypes.c_char_p])


def core_is_nick_name_valid(name):
    return _fn(_capi.enc(name))
