import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_PlayNode", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_bool])


def npc_play_node(npc, node_id, move_type, move_speed, radius, set_angle):
    return _fn(npc, node_id, move_type, move_speed, radius, set_angle)
