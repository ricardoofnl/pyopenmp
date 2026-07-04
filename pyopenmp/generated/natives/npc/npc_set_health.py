import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetHealth", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float])


def npc_set_health(npc, health):
    return _fn(npc, health)
