import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Actor_GetHealth", ctypes.c_float, [ctypes.c_void_p])


def actor_get_health(actor):
    return _fn(actor)
