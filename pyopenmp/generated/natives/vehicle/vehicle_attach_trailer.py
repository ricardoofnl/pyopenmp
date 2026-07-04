import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_AttachTrailer", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def vehicle_attach_trailer(trailer, vehicle):
    return _fn(trailer, vehicle)
