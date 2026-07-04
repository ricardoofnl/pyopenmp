import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("GangZone_GetID", ctypes.c_int, [ctypes.c_void_p])


def gang_zone_get_id(gangzone):
    return _fn(gangzone)
