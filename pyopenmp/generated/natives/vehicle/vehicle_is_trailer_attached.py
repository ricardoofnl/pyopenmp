import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_IsTrailerAttached", ctypes.c_bool, [ctypes.c_void_p])


def vehicle_is_trailer_attached(vehicle):
    return _fn(vehicle)
