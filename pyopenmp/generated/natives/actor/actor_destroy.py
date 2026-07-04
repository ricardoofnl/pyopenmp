import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Actor_Destroy", ctypes.c_bool, [ctypes.c_void_p])


def actor_destroy(actor):
    return _fn(actor)
