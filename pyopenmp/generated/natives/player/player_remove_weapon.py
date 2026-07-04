import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_RemoveWeapon", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def player_remove_weapon(player, weapon):
    return _fn(player, weapon)
