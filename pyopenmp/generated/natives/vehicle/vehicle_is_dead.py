import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_IsDead", ctypes.c_bool, [ctypes.c_void_p])


def vehicle_is_dead(vehicle):
    return _fn(vehicle)
