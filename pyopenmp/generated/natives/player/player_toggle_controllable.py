import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_ToggleControllable", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_bool])


def player_toggle_controllable(player, enable):
    return _fn(player, enable)
