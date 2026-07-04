import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_IsPlayingNode", ctypes.c_bool, [ctypes.c_void_p])


def npc_is_playing_node(npc):
    return _fn(npc)
