import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_IsNickNameCharacterAllowed", ctypes.c_bool, [ctypes.c_int])


def core_is_nick_name_character_allowed(character):
    return _fn(character)
