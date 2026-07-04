import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_IsStreamedIn", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def vehicle_is_streamed_in(vehicle, player):
    return _fn(vehicle, player)
