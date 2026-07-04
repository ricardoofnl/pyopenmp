import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_LinkToInterior", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def vehicle_link_to_interior(vehicle, interiorid):
    return _fn(vehicle, interiorid)
