import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_IsWidescreenToggled", ctypes.c_bool, [ctypes.c_void_p])


def player_is_widescreen_toggled(player):
    return _fn(player)
