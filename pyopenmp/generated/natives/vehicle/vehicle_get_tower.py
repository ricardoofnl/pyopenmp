import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetTower", ctypes.c_void_p, [ctypes.c_void_p])


def vehicle_get_tower(vehicle):
    return _fn(vehicle)
