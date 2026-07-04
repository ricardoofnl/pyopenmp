import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_Shoot", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_uint8, ctypes.c_int, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_bool, ctypes.c_uint8])


def npc_shoot(npc, weapon, hit_id, hit_type, end_x, end_y, end_z, offset_x, offset_y, offset_z, is_hit, check_in_between_flags):
    return _fn(npc, weapon, hit_id, hit_type, end_x, end_y, end_z, offset_x, offset_y, offset_z, is_hit, check_in_between_flags)
