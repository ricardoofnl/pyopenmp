import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_SetRespawnDelay", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def vehicle_set_respawn_delay(vehicle, respawn_delay):
    return _fn(vehicle, respawn_delay)
