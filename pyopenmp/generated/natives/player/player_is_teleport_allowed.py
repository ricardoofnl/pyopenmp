import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_IsTeleportAllowed", ctypes.c_bool, [ctypes.c_void_p])


def player_is_teleport_allowed(player):
    return _fn(player)
