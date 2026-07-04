import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_ChangeColor", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_int])


def vehicle_change_color(vehicle, color1, color2):
    return _fn(vehicle, color1, color2)
