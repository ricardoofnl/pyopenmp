import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Actor_SetFacingAngle", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float])


def actor_set_facing_angle(actor, angle):
    return _fn(actor, angle)
