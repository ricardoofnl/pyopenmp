import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_MoveToPlayer", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_int, ctypes.c_bool])


def npc_move_to_player(npc, player, move_type, move_speed, stop_range, pos_check_update_delay, auto_restart):
    return _fn(npc, player, move_type, move_speed, stop_range, pos_check_update_delay, auto_restart)
