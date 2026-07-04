import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetLandingGearState", ctypes.c_int, [ctypes.c_void_p])


def vehicle_get_landing_gear_state(vehicle):
    return _fn(vehicle)
