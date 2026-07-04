import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_SetSpawnInfo", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int])


def vehicle_set_spawn_info(vehicle, modelid, x, y, z, rotation, color1, color2, respawn_time, interior):
    return _fn(vehicle, modelid, x, y, z, rotation, color1, color2, respawn_time, interior)
