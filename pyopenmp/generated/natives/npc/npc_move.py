import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_Move", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_int, ctypes.c_float, ctypes.c_float])


def npc_move(npc, x, y, z, move_type, move_speed, stop_range):
    return _fn(npc, x, y, z, move_type, move_speed, stop_range)
