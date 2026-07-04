import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetArmour", ctypes.c_float, [ctypes.c_void_p])


def npc_get_armour(npc):
    return _fn(npc)
