import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetSurfingPlayerObject", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int])


def npc_set_surfing_player_object(npc, player, object_id):
    return _fn(npc, player, object_id)
