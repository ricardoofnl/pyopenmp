import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Recording_Stop", ctypes.c_bool, [ctypes.c_void_p])


def recording_stop(player):
    return _fn(player)
