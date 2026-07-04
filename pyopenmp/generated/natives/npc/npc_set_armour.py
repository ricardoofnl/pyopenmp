import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetArmour", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float])


def npc_set_armour(npc, armour):
    return _fn(npc, armour)
