import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetAnimation", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_float, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_int])


def npc_set_animation(npc, animation_id, delta, loop, lock_x, lock_y, freeze, time):
    return _fn(npc, animation_id, delta, loop, lock_x, lock_y, freeze, time)
