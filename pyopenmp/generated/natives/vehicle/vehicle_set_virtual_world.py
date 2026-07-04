import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_SetVirtualWorld", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def vehicle_set_virtual_world(vehicle, virtual_world):
    return _fn(vehicle, virtual_world)
