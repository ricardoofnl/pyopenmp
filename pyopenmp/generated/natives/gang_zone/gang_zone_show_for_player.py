import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("GangZone_ShowForPlayer", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32])


def gang_zone_show_for_player(player, gangzone, color):
    return _fn(player, gangzone, color)
