import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_FromID", ctypes.c_void_p, [ctypes.c_int])


def npc_from_id(npcid):
    return _fn(npcid)
