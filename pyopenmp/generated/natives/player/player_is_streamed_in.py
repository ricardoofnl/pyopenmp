import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_IsStreamedIn", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def player_is_streamed_in(player, other):
    return _fn(player, other)
