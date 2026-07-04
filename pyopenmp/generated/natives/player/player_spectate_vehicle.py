import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SpectateVehicle", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int])


def player_spectate_vehicle(player, target, mode):
    return _fn(player, target, mode)
