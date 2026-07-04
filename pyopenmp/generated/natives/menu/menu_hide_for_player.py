import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Menu_HideForPlayer", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def menu_hide_for_player(menu, player):
    return _fn(menu, player)
