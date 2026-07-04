import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_GetType", ctypes.c_uint8, [ctypes.c_void_p, ctypes.c_int])


def object_get_type(player, objectid):
    return _fn(player, objectid)
