import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetTargetActor", ctypes.c_void_p, [ctypes.c_void_p])


def player_get_target_actor(player):
    return _fn(player)
