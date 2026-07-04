import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_IsOccupied", ctypes.c_bool, [ctypes.c_void_p])


def vehicle_is_occupied(vehicle):
    return _fn(vehicle)
