import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerObject_SetRot", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def player_object_set_rot(player, object, rotation_x, rotation_y, rotation_z):
    return _fn(player, object, rotation_x, rotation_y, rotation_z)
