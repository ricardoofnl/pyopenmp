import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Class_Count", ctypes.c_int, [])


def class_count():
    return _fn()
