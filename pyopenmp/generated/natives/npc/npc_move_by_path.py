import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_MoveByPath", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_float, ctypes.c_bool])


def npc_move_by_path(npc, path_id, move_type, move_speed, reverse):
    return _fn(npc, path_id, move_type, move_speed, reverse)
