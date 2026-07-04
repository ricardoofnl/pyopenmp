import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetHydraReactorAngle", ctypes.c_uint32, [ctypes.c_void_p])


def player_get_hydra_reactor_angle(player):
    return _fn(player)
