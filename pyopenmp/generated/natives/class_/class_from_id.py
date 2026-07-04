import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Class_FromID", ctypes.c_void_p, [ctypes.c_int])


def class_from_id(classid):
    return _fn(classid)
