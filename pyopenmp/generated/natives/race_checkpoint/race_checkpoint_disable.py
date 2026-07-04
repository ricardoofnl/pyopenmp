import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("RaceCheckpoint_Disable", ctypes.c_bool, [ctypes.c_void_p])


def race_checkpoint_disable(player):
    return _fn(player)
