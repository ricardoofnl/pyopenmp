import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetID", ctypes.c_int, [ctypes.c_void_p])


def npc_get_id(npc):
    return _fn(npc)
