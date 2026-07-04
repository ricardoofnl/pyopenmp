import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetWeaponState", ctypes.c_int, [ctypes.c_void_p])


def npc_get_weapon_state(npc):
    return _fn(npc)
