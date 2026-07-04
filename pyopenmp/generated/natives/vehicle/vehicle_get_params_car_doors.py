import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetParamsCarDoors", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)])


def vehicle_get_params_car_doors(vehicle):
    front_left = ctypes.c_int()
    front_right = ctypes.c_int()
    rear_left = ctypes.c_int()
    rear_right = ctypes.c_int()
    __ret = _fn(vehicle, ctypes.byref(front_left), ctypes.byref(front_right), ctypes.byref(rear_left), ctypes.byref(rear_right))
    if __ret:
        return (front_left.value, front_right.value, rear_left.value, rear_right.value)
    return None
