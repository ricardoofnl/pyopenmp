import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Actor_IsValid", ctypes.c_bool, [ctypes.c_void_p])


def actor_is_valid(actor):
    return _fn(actor)
