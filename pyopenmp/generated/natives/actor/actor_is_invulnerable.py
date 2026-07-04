import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Actor_IsInvulnerable", ctypes.c_bool, [ctypes.c_void_p])


def actor_is_invulnerable(actor):
    return _fn(actor)
