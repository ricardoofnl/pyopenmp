import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetWeaponActualClipSize", ctypes.c_int, [ctypes.c_void_p, ctypes.c_int])


def npc_get_weapon_actual_clip_size(npc, weapon):
    return _fn(npc, weapon)
