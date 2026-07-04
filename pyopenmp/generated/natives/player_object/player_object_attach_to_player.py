import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerObject_AttachToPlayer", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def player_object_attach_to_player(player, object, player_attached_to, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z):
    return _fn(player, object, player_attached_to, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z)
