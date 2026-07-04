import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_FromID", ctypes.c_void_p, [ctypes.c_int])


def object_from_id(objectid):
    return _fn(objectid)
