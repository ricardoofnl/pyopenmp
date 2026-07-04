import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_AllowTeleport", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_bool])


def player_allow_teleport(player, allow):
    return _fn(player, allow)
