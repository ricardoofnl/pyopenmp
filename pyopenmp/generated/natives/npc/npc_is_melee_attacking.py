import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_IsMeleeAttacking", ctypes.c_bool, [ctypes.c_void_p])


def npc_is_melee_attacking(npc):
    return _fn(npc)
