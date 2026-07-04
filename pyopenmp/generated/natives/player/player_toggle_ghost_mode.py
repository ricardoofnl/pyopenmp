import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_ToggleGhostMode", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_bool])


def player_toggle_ghost_mode(player, toggle):
    return _fn(player, toggle)
