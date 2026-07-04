import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_DisableRemoteVehicleCollisions", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_bool])


def player_disable_remote_vehicle_collisions(player, disable):
    return _fn(player, disable)
