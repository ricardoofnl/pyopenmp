import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Actor_GetVirtualWorld", ctypes.c_int, [ctypes.c_void_p])


def actor_get_virtual_world(actor):
    return _fn(actor)
