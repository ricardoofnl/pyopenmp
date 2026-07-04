import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetInterior", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def player_set_interior(player, interior):
    return _fn(player, interior)
