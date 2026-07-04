import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetOccupiedTick", ctypes.c_int, [ctypes.c_void_p])


def vehicle_get_occupied_tick(vehicle):
    return _fn(vehicle)
