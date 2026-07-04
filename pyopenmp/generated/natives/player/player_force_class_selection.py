import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_ForceClassSelection", ctypes.c_bool, [ctypes.c_void_p])


def player_force_class_selection(player):
    return _fn(player)
