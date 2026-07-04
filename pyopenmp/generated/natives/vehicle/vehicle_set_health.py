import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_SetHealth", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float])


def vehicle_set_health(vehicle, health):
    return _fn(vehicle, health)
