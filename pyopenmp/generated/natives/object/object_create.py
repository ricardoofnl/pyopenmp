import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_Create", ctypes.c_void_p, [ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.POINTER(ctypes.c_int)])


def object_create(modelid, x, y, z, rotation_x, rotation_y, rotation_z, draw_distance):
    id = ctypes.c_int()
    __ret = _fn(modelid, x, y, z, rotation_x, rotation_y, rotation_z, draw_distance, ctypes.byref(id))
    return (__ret, id.value)
