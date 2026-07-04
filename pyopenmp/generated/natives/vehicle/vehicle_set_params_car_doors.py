import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_SetParamsCarDoors", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int])


def vehicle_set_params_car_doors(vehicle, front_left, front_right, rear_left, rear_right):
    return _fn(vehicle, front_left, front_right, rear_left, rear_right)
