import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetSpecialAction", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_uint32])


def player_set_special_action(player, action):
    return _fn(player, action)
