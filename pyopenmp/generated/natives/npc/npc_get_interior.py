import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetInterior", ctypes.c_int, [ctypes.c_void_p])


def npc_get_interior(npc):
    return _fn(npc)
