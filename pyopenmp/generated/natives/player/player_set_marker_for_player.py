import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetMarkerForPlayer", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32])


def player_set_marker_for_player(player, other, color):
    return _fn(player, other, color)
