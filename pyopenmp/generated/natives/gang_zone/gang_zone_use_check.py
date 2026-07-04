import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("GangZone_UseCheck", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_bool])


def gang_zone_use_check(gangzone, enable):
    return _fn(gangzone, enable)
