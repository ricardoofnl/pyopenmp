import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_UpdateDamageStatus", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int])


def vehicle_update_damage_status(vehicle, panels, doors, lights, tires):
    return _fn(vehicle, panels, doors, lights, tires)
