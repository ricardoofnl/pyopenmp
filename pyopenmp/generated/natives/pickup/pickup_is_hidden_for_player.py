import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Pickup_IsHiddenForPlayer", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def pickup_is_hidden_for_player(player, pickup):
    return _fn(player, pickup)
