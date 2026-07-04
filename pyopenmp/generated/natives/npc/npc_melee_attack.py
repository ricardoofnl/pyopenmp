import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_MeleeAttack", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_bool])


def npc_melee_attack(npc, time, secondary_attack):
    return _fn(npc, time, secondary_attack)
