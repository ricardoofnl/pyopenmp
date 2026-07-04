import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_EnableFriendlyFire", ctypes.c_bool, [])


def vehicle_enable_friendly_fire():
    return _fn()
