import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_SetPos", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def vehicle_set_pos(vehicle, x, y, z):
    return _fn(vehicle, x, y, z)
