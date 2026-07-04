import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetSkin", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def player_set_skin(player, skin):
    return _fn(player, skin)
