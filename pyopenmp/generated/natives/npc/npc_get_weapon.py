import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetWeapon", ctypes.c_uint8, [ctypes.c_void_p])


def npc_get_weapon(npc):
    return _fn(npc)
