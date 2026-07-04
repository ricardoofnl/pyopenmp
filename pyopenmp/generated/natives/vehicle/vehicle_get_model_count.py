import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetModelCount", ctypes.c_int, [ctypes.c_int])


def vehicle_get_model_count(modelid):
    return _fn(modelid)
