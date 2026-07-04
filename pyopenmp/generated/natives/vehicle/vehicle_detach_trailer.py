import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_DetachTrailer", ctypes.c_bool, [ctypes.c_void_p])


def vehicle_detach_trailer(vehicle):
    return _fn(vehicle)
