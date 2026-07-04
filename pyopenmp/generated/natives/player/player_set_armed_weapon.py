import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetArmedWeapon", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_uint8])


def player_set_armed_weapon(player, weapon):
    return _fn(player, weapon)
