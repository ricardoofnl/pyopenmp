import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetVirtualWorld", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def player_set_virtual_world(player, vw):
    return _fn(player, vw)
