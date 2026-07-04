import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_IsCuffed", ctypes.c_bool, [ctypes.c_void_p])


def player_is_cuffed(player):
    return _fn(player)
