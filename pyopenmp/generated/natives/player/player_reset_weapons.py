import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_ResetWeapons", ctypes.c_bool, [ctypes.c_void_p])


def player_reset_weapons(player):
    return _fn(player)
