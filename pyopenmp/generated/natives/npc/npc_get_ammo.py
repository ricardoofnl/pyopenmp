import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetAmmo", ctypes.c_int, [ctypes.c_void_p])


def npc_get_ammo(npc):
    return _fn(npc)
