import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GiveWeapon", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_int])


def player_give_weapon(player, weapon, ammo):
    return _fn(player, weapon, ammo)
