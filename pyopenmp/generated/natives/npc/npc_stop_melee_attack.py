import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_StopMeleeAttack", ctypes.c_bool, [ctypes.c_void_p])


def npc_stop_melee_attack(npc):
    return _fn(npc)
