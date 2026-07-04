import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetAmmo", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def npc_set_ammo(npc, ammo):
    return _fn(npc, ammo)
