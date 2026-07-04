import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetWeaponShootTime", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_int])


def npc_set_weapon_shoot_time(npc, weapon, time):
    return _fn(npc, weapon, time)
