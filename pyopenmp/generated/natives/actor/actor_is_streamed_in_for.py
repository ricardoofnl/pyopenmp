import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Actor_IsStreamedInFor", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def actor_is_streamed_in_for(actor, player):
    return _fn(actor, player)
