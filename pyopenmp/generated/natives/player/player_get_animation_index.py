import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetAnimationIndex", ctypes.c_int, [ctypes.c_void_p])


def player_get_animation_index(player):
    return _fn(player)
