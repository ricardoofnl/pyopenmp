import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_CountOccupants", ctypes.c_int, [ctypes.c_void_p])


def vehicle_count_occupants(vehicle):
    return _fn(vehicle)
