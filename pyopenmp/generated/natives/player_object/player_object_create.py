import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerObject_Create", ctypes.c_void_p, [ctypes.c_void_p, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.POINTER(ctypes.c_int)])


def player_object_create(player, modelid, x, y, z, rotation_x, rotation_y, rotation_z, draw_distance):
    id = ctypes.c_int()
    __ret = _fn(player, modelid, x, y, z, rotation_x, rotation_y, rotation_z, draw_distance, ctypes.byref(id))
    return (__ret, id.value)
