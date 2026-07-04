import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetTrainSpeed", ctypes.c_float, [ctypes.c_void_p])


def vehicle_get_train_speed(vehicle):
    return _fn(vehicle)
