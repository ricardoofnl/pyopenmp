import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerObject_Stop", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def player_object_stop(player, object):
    return _fn(player, object)
