import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Checkpoint_Set", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def checkpoint_set(player, x, y, z, radius):
    return _fn(player, x, y, z, radius)
