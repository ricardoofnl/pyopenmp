import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_IsAnimationLibraryValid", ctypes.c_bool, [ctypes.c_char_p])


def core_is_animation_library_valid(name):
    return _fn(_capi.enc(name))
