import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetWeaponAccuracy", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_float])


def npc_set_weapon_accuracy(npc, weapon, accuracy):
    return _fn(npc, weapon, accuracy)
