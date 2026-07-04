import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_SetRot", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def object_set_rot(object, rotation_x, rotation_y, rotation_z):
    return _fn(object, rotation_x, rotation_y, rotation_z)
