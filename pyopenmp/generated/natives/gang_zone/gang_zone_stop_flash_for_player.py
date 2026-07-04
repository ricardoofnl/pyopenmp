import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("GangZone_StopFlashForPlayer", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def gang_zone_stop_flash_for_player(player, gangzone):
    return _fn(player, gangzone)
