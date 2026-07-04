import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetWeaponShootTime", ctypes.c_int, [ctypes.c_void_p, ctypes.c_int])


def npc_get_weapon_shoot_time(npc, weapon):
    return _fn(npc, weapon)
