import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerObject_Destroy", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def player_object_destroy(player, object):
    return _fn(player, object)
