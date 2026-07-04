import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetOccupant", ctypes.c_void_p, [ctypes.c_void_p, ctypes.c_int])


def vehicle_get_occupant(vehicle, seat):
    return _fn(vehicle, seat)
