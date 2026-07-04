import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetVirtualWorld", ctypes.c_int, [ctypes.c_void_p])


def npc_get_virtual_world(npc):
    return _fn(npc)
