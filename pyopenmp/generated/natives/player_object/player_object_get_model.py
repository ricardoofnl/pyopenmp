import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerObject_GetModel", ctypes.c_int, [ctypes.c_void_p, ctypes.c_void_p])


def player_object_get_model(player, object):
    return _fn(player, object)
