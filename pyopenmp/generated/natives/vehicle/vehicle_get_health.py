import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetHealth", ctypes.c_float, [ctypes.c_void_p])


def vehicle_get_health(vehicle):
    return _fn(vehicle)
