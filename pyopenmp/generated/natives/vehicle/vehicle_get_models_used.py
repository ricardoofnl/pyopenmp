import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetModelsUsed", ctypes.c_int, [])


def vehicle_get_models_used():
    return _fn()
