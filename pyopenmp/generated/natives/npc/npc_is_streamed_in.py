import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_IsStreamedIn", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def npc_is_streamed_in(npc, player):
    return _fn(npc, player)
