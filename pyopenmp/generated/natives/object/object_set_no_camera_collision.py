import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_SetNoCameraCollision", ctypes.c_bool, [ctypes.c_void_p])


def object_set_no_camera_collision(object):
    return _fn(object)
