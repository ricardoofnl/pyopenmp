import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetRespawnTick", ctypes.c_int, [ctypes.c_void_p])


def vehicle_get_respawn_tick(vehicle):
    return _fn(vehicle)
