import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_IsSirenEnabled", ctypes.c_bool, [ctypes.c_void_p])


def vehicle_is_siren_enabled(vehicle):
    return _fn(vehicle)
