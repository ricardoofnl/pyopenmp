import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Actor_GetFacingAngle", ctypes.c_float, [ctypes.c_void_p])


def actor_get_facing_angle(actor):
    return _fn(actor)
