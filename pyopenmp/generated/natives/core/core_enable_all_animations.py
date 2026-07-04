import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_EnableAllAnimations", ctypes.c_bool, [ctypes.c_bool])


def core_enable_all_animations(allow):
    return _fn(allow)
