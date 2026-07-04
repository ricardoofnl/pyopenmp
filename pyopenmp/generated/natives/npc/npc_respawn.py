import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_Respawn", ctypes.c_bool, [ctypes.c_void_p])


def npc_respawn(npc):
    return _fn(npc)
