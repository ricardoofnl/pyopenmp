import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetHydraReactorAngle", ctypes.c_uint32, [ctypes.c_void_p])


def vehicle_get_hydra_reactor_angle(vehicle):
    return _fn(vehicle)
