import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Actor_SetVirtualWorld", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def actor_set_virtual_world(actor, vw):
    return _fn(actor, vw)
