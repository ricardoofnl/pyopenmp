import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_IsInAnyVehicle", ctypes.c_bool, [ctypes.c_void_p])


def player_is_in_any_vehicle(player):
    return _fn(player)
