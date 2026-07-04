import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetSurfingObject", ctypes.c_int, [ctypes.c_void_p])


def npc_get_surfing_object(npc):
    return _fn(npc)
