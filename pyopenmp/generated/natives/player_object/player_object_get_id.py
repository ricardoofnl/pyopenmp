import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerObject_GetID", ctypes.c_int, [ctypes.c_void_p, ctypes.c_void_p])


def player_object_get_id(player, object):
    return _fn(player, object)
