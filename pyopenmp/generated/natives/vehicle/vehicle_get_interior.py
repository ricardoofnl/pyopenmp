import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetInterior", ctypes.c_int, [ctypes.c_void_p])


def vehicle_get_interior(vehicle):
    return _fn(vehicle)
