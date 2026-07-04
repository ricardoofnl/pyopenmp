import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_AreAllAnimationsEnabled", ctypes.c_bool, [])


def core_are_all_animations_enabled():
    return _fn()
