import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("GangZone_IsPlayerIn", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def gang_zone_is_player_in(player, gangzone):
    return _fn(player, gangzone)
