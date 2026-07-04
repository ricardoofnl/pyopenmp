import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_SetZAngle", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float])


def vehicle_set_z_angle(vehicle, angle):
    return _fn(vehicle, angle)
