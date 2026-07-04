import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("GangZone_Destroy", ctypes.c_bool, [ctypes.c_void_p])


def gang_zone_destroy(gangzone):
    return _fn(gangzone)
