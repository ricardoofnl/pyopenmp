import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetComponentType", ctypes.c_int, [ctypes.c_int])


def vehicle_get_component_type(componentid):
    return _fn(componentid)
