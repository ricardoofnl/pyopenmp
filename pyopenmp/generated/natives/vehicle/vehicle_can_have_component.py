import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_CanHaveComponent", ctypes.c_bool, [ctypes.c_int, ctypes.c_int])


def vehicle_can_have_component(modelid, componentid):
    return _fn(modelid, componentid)
