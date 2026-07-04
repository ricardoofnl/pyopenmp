import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_AimAtPlayer", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_int, ctypes.c_bool, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_uint8])


def npc_aim_at_player(npc, at_player, shoot, shoot_delay, update_angle, offset_x, offset_y, offset_z, offset_from_x, offset_from_y, offset_from_z, check_in_between_flags):
    return _fn(npc, at_player, shoot, shoot_delay, update_angle, offset_x, offset_y, offset_z, offset_from_x, offset_from_y, offset_from_z, check_in_between_flags)
