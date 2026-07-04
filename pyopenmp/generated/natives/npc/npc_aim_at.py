import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_AimAt", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_bool, ctypes.c_int, ctypes.c_bool, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_uint8])


def npc_aim_at(npc, x, y, z, shoot, shoot_delay, update_angle, offset_from_x, offset_from_y, offset_from_z, check_in_between_flags):
    return _fn(npc, x, y, z, shoot, shoot_delay, update_angle, offset_from_x, offset_from_y, offset_from_z, check_in_between_flags)
