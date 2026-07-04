import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_PutInVehicle", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int])


def player_put_in_vehicle(player, vehicle, seat):
    return _fn(player, vehicle, seat)
