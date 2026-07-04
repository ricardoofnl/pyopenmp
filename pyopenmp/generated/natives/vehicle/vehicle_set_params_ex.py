import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_SetParamsEx", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int])


def vehicle_set_params_ex(vehicle, engine, lights, alarm, doors, bonnet, boot, objective):
    return _fn(vehicle, engine, lights, alarm, doors, bonnet, boot, objective)
