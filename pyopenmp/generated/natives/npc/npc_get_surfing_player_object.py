import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetSurfingPlayerObject", ctypes.c_int, [ctypes.c_void_p])


def npc_get_surfing_player_object(npc):
    return _fn(npc)
