import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetRespawnDelay", ctypes.c_int, [ctypes.c_void_p])


def vehicle_get_respawn_delay(vehicle):
    return _fn(vehicle)
