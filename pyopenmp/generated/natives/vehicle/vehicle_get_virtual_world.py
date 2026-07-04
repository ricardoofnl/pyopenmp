import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetVirtualWorld", ctypes.c_int, [ctypes.c_void_p])


def vehicle_get_virtual_world(vehicle):
    return _fn(vehicle)
