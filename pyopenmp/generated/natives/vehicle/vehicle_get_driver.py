import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetDriver", ctypes.c_void_p, [ctypes.c_void_p])


def vehicle_get_driver(vehicle):
    return _fn(vehicle)
