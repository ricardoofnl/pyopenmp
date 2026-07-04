import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetWeapon", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_uint8])


def npc_set_weapon(npc, weapon):
    return _fn(npc, weapon)
