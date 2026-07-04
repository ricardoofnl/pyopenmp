import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Checkpoint_Disable", ctypes.c_bool, [ctypes.c_void_p])


def checkpoint_disable(player):
    return _fn(player)
