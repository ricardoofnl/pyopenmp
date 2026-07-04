import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("GangZone_ShowForAll", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_uint32])


def gang_zone_show_for_all(gangzone, color):
    return _fn(gangzone, color)
