import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_IsNPC", ctypes.c_bool, [ctypes.c_void_p])


def player_is_npc(player):
    return _fn(player)
