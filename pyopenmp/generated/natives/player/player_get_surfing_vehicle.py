import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetSurfingVehicle", ctypes.c_void_p, [ctypes.c_void_p])


def player_get_surfing_vehicle(player):
    return _fn(player)
