import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_SetToRespawn", ctypes.c_bool, [ctypes.c_void_p])


def vehicle_set_to_respawn(vehicle):
    return _fn(vehicle)
