import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerObject_IsNoCameraCollision", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def player_object_is_no_camera_collision(player, object):
    return _fn(player, object)
