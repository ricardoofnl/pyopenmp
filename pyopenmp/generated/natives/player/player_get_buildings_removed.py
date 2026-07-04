import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetBuildingsRemoved", ctypes.c_int, [ctypes.c_void_p])


def player_get_buildings_removed(player):
    return _fn(player)
