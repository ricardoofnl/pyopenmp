import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Checkpoint_IsPlayerIn", ctypes.c_bool, [ctypes.c_void_p])


def checkpoint_is_player_in(player):
    return _fn(player)
