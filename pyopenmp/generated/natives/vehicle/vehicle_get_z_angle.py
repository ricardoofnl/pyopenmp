import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetZAngle", ctypes.c_float, [ctypes.c_void_p])


def vehicle_get_z_angle(vehicle):
    return _fn(vehicle)
