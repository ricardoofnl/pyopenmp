import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Actor_ClearAnimations", ctypes.c_bool, [ctypes.c_void_p])


def actor_clear_animations(actor):
    return _fn(actor)
