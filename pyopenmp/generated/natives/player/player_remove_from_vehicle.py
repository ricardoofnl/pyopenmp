import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_RemoveFromVehicle", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_bool])


def player_remove_from_vehicle(player, force):
    return _fn(player, force)
