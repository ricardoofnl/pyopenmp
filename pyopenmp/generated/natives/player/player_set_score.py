import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetScore", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def player_set_score(player, score):
    return _fn(player, score)
