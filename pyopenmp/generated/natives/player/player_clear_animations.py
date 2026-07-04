import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_ClearAnimations", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def player_clear_animations(player, sync_type):
    return _fn(player, sync_type)
