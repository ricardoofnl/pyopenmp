import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_SetDefaultCameraCollision", ctypes.c_bool, [ctypes.c_bool])


def object_set_default_camera_collision(disable):
    return _fn(disable)
