import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetPaintjob", ctypes.c_int, [ctypes.c_void_p])


def vehicle_get_paintjob(vehicle):
    return _fn(vehicle)
