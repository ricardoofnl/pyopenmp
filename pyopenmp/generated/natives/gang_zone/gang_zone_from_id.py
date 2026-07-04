import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("GangZone_FromID", ctypes.c_void_p, [ctypes.c_int])


def gang_zone_from_id(gangzoneid):
    return _fn(gangzoneid)
