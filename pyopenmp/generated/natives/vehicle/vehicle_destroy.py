import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_Destroy", ctypes.c_bool, [ctypes.c_void_p])


def vehicle_destroy(vehicle):
    return _fn(vehicle)
