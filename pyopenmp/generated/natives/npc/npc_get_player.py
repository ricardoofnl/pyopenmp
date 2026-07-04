import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetPlayer", ctypes.c_void_p, [ctypes.c_void_p])


def npc_get_player(npc):
    return _fn(npc)
