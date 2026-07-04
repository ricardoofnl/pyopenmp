import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_EnableZoneNames", ctypes.c_bool, [ctypes.c_bool])


def core_enable_zone_names(enable):
    return _fn(enable)
