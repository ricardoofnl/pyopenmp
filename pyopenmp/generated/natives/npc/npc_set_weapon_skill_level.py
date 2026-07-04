import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetWeaponSkillLevel", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_uint8, ctypes.c_int])


def npc_set_weapon_skill_level(npc, skill, level):
    return _fn(npc, skill, level)
