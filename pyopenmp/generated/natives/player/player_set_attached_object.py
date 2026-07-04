import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetAttachedObject", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_uint32, ctypes.c_uint32])


def player_set_attached_object(player, index, modelid, bone, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z, scale_x, scale_y, scale_z, materialcolor1, materialcolor2):
    return _fn(player, index, modelid, bone, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z, scale_x, scale_y, scale_z, materialcolor1, materialcolor2)
