import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetCab", ctypes.c_void_p, [ctypes.c_void_p])


def vehicle_get_cab(vehicle):
    return _fn(vehicle)
