import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_IsAimingAtPlayer", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def npc_is_aiming_at_player(npc, at_player):
    return _fn(npc, at_player)
