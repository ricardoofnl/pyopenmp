import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetSirenState", ctypes.c_int, [ctypes.c_void_p])


def vehicle_get_siren_state(vehicle):
    return _fn(vehicle)
