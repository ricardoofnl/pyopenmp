import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Actor_GetID", ctypes.c_int, [ctypes.c_void_p])


def actor_get_id(actor):
    return _fn(actor)
