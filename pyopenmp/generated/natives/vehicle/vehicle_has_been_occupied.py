import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_HasBeenOccupied", ctypes.c_bool, [ctypes.c_void_p])


def vehicle_has_been_occupied(vehicle):
    return _fn(vehicle)
