import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Actor_SetHealth", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float])


def actor_set_health(actor, hp):
    return _fn(actor, hp)
