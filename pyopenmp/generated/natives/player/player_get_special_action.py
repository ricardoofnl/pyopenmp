import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetSpecialAction", ctypes.c_int, [ctypes.c_void_p])


def player_get_special_action(player):
    return _fn(player)
