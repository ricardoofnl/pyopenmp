import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetWeaponClipSize", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_int])


def npc_set_weapon_clip_size(npc, weapon, size):
    return _fn(npc, weapon, size)
