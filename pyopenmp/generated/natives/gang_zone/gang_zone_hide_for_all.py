import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("GangZone_HideForAll", ctypes.c_bool, [ctypes.c_void_p])


def gang_zone_hide_for_all(gangzone):
    return _fn(gangzone)
