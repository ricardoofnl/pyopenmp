import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetDamageStatus", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)])


def vehicle_get_damage_status(vehicle):
    panels = ctypes.c_int()
    doors = ctypes.c_int()
    lights = ctypes.c_int()
    tires = ctypes.c_int()
    __ret = _fn(vehicle, ctypes.byref(panels), ctypes.byref(doors), ctypes.byref(lights), ctypes.byref(tires))
    if __ret:
        return (panels.value, doors.value, lights.value, tires.value)
    return None
