import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_Move", ctypes.c_int, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def object_move(object, x, y, z, speed, rotation_x, rotation_y, rotation_z):
    return _fn(object, x, y, z, speed, rotation_x, rotation_y, rotation_z)
