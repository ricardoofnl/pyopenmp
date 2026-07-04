import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("RaceCheckpoint_Set", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def race_checkpoint_set(player, type, x, y, z, next_x, next_y, next_z, radius):
    return _fn(player, type, x, y, z, next_x, next_y, next_z, radius)
