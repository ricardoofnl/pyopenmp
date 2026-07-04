import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_ToggleClock", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_bool])


def player_toggle_clock(player, enable):
    return _fn(player, enable)
