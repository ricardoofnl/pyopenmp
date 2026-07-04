import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_IsInVehicle", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def player_is_in_vehicle(player, target_vehicle):
    return _fn(player, target_vehicle)
