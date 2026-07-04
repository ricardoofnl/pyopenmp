import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetSirenState", ctypes.c_int, [ctypes.c_void_p])


def player_get_siren_state(player):
    return _fn(player)
