import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_ApplyAnimation", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_float, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_int])


def npc_apply_animation(npc, animlib, animname, delta, loop, lock_x, lock_y, freeze, time):
    return _fn(npc, _capi.enc(animlib), _capi.enc(animname), delta, loop, lock_x, lock_y, freeze, time)
