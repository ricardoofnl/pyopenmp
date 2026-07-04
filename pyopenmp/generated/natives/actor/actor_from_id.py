import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Actor_FromID", ctypes.c_void_p, [ctypes.c_int])


def actor_from_id(actorid):
    return _fn(actorid)
