import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerObject_IsValid", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def player_object_is_valid(player, object):
    return _fn(player, object)
