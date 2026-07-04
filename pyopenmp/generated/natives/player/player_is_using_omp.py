import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_IsUsingOmp", ctypes.c_bool, [ctypes.c_void_p])


def player_is_using_omp(player):
    return _fn(player)
