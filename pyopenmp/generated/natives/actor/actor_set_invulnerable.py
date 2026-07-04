import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Actor_SetInvulnerable", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_bool])


def actor_set_invulnerable(actor, toggle):
    return _fn(actor, toggle)
