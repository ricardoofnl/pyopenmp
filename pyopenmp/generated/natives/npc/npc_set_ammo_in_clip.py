import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetAmmoInClip", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def npc_set_ammo_in_clip(npc, ammo):
    return _fn(npc, ammo)
