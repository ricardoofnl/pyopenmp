import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_GetSyncRotation", ctypes.c_bool, [ctypes.c_void_p])


def object_get_sync_rotation(object):
    return _fn(object)
