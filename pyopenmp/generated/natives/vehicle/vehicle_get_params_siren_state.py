import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetParamsSirenState", ctypes.c_int, [ctypes.c_void_p])


def vehicle_get_params_siren_state(vehicle):
    return _fn(vehicle)
