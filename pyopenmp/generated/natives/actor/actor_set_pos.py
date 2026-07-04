import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Actor_SetPos", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def actor_set_pos(actor, x, y, z):
    return _fn(actor, x, y, z)
