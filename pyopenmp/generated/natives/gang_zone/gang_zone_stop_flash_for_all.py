import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("GangZone_StopFlashForAll", ctypes.c_bool, [ctypes.c_void_p])


def gang_zone_stop_flash_for_all(gangzone):
    return _fn(gangzone)
