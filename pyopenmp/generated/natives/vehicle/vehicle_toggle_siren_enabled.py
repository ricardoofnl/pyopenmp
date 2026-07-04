import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_ToggleSirenEnabled", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_bool])


def vehicle_toggle_siren_enabled(vehicle, status):
    return _fn(vehicle, status)
