import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerObject_GetSyncRotation", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def player_object_get_sync_rotation(player, object):
    return _fn(player, object)
