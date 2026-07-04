import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetWeaponAccuracy", ctypes.c_float, [ctypes.c_void_p, ctypes.c_int])


def npc_get_weapon_accuracy(npc, weapon):
    return _fn(npc, weapon)
