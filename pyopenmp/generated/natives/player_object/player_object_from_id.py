import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerObject_FromID", ctypes.c_void_p, [ctypes.c_void_p, ctypes.c_int])


def player_object_from_id(player, objectid):
    return _fn(player, objectid)
