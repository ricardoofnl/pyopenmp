import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_AllowNickNameCharacter", ctypes.c_bool, [ctypes.c_int, ctypes.c_bool])


def core_allow_nick_name_character(character, allow):
    return _fn(character, allow)
