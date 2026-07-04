import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_RemoveMapIcon", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def player_remove_map_icon(player, icon):
    return _fn(player, icon)
