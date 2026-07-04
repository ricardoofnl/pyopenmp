import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_AreWeaponsAllowed", ctypes.c_bool, [ctypes.c_void_p])


def player_are_weapons_allowed(player):
    return _fn(player)
