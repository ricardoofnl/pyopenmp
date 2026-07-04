import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetVehicleSeat", ctypes.c_int, [ctypes.c_void_p])


def player_get_vehicle_seat(player):
    return _fn(player)
