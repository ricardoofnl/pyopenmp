import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetDistanceFromPoint", ctypes.c_float, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def vehicle_get_distance_from_point(vehicle, x, y, z):
    return _fn(vehicle, x, y, z)
