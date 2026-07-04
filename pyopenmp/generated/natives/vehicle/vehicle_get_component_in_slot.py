import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetComponentInSlot", ctypes.c_int, [ctypes.c_void_p, ctypes.c_int])


def vehicle_get_component_in_slot(vehicle, slot):
    return _fn(vehicle, slot)
