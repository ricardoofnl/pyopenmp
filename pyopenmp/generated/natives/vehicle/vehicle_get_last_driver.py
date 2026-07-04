import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetLastDriver", ctypes.c_void_p, [ctypes.c_void_p])


def vehicle_get_last_driver(vehicle):
    return _fn(vehicle)
