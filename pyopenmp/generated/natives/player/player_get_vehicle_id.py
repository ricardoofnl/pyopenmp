import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetVehicleID", ctypes.c_int, [ctypes.c_void_p])


def player_get_vehicle_id(player):
    return _fn(player)
