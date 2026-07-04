import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetInvulnerable", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_bool])


def npc_set_invulnerable(npc, toggle):
    return _fn(npc, toggle)
