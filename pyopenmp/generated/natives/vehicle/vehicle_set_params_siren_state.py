import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_SetParamsSirenState", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_bool])


def vehicle_set_params_siren_state(vehicle, siren_state):
    return _fn(vehicle, siren_state)
