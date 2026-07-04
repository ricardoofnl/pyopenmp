import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_AddComponent", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def vehicle_add_component(vehicle, componentid):
    return _fn(vehicle, componentid)
