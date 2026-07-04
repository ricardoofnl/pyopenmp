import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("GangZone_GetColorForPlayer", ctypes.c_int, [ctypes.c_void_p, ctypes.c_void_p])


def gang_zone_get_color_for_player(player, gangzone):
    return _fn(player, gangzone)
