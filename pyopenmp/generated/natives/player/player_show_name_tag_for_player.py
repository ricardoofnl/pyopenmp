import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_ShowNameTagForPlayer", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool])


def player_show_name_tag_for_player(player, other, enable):
    return _fn(player, other, enable)
