import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetWeaponSkillLevel", ctypes.c_int, [ctypes.c_void_p, ctypes.c_int])


def npc_get_weapon_skill_level(npc, skill):
    return _fn(npc, skill)
