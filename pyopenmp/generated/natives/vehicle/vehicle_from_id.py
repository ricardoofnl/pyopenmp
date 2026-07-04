import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_FromID", ctypes.c_void_p, [ctypes.c_int])


def vehicle_from_id(vehicleid):
    return _fn(vehicleid)
