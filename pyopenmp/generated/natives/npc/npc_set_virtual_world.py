import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetVirtualWorld", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def npc_set_virtual_world(npc, virtual_world):
    return _fn(npc, virtual_world)
