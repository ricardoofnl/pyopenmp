import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("RaceCheckpoint_IsActive", ctypes.c_bool, [ctypes.c_void_p])


def race_checkpoint_is_active(player):
    return _fn(player)
