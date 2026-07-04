import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetModel", ctypes.c_int, [ctypes.c_void_p])


def vehicle_get_model(vehicle):
    return _fn(vehicle)
