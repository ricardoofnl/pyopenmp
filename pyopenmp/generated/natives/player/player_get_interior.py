import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetInterior", ctypes.c_int, [ctypes.c_void_p])


def player_get_interior(player):
    return _fn(player)
