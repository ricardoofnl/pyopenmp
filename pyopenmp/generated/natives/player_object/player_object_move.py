import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerObject_Move", ctypes.c_int, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def player_object_move(player, object, x, y, z, speed, rotation_x, rotation_y, rotation_z):
    return _fn(player, object, x, y, z, speed, rotation_x, rotation_y, rotation_z)
