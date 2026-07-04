import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_SetParamsForPlayer", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int])


def vehicle_set_params_for_player(vehicle, player, objective, doors):
    return _fn(vehicle, player, objective, doors)
