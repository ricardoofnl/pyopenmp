import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetMarkerForPlayer", ctypes.c_uint32, [ctypes.c_void_p, ctypes.c_void_p])


def player_get_marker_for_player(player, other):
    return _fn(player, other)
