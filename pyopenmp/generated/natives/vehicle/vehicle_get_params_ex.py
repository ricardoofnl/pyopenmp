import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetParamsEx", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)])


def vehicle_get_params_ex(vehicle):
    engine = ctypes.c_int()
    lights = ctypes.c_int()
    alarm = ctypes.c_int()
    doors = ctypes.c_int()
    bonnet = ctypes.c_int()
    boot = ctypes.c_int()
    objective = ctypes.c_int()
    __ret = _fn(vehicle, ctypes.byref(engine), ctypes.byref(lights), ctypes.byref(alarm), ctypes.byref(doors), ctypes.byref(bonnet), ctypes.byref(boot), ctypes.byref(objective))
    if __ret:
        return (engine.value, lights.value, alarm.value, doors.value, bonnet.value, boot.value, objective.value)
    return None
