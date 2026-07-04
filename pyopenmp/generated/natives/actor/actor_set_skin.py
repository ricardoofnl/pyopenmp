import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Actor_SetSkin", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def actor_set_skin(actor, skin):
    return _fn(actor, skin)
