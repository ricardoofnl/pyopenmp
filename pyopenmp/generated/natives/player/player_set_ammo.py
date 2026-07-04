import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetAmmo", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_uint8, ctypes.c_uint32])


def player_set_ammo(player, id, ammo):
    return _fn(player, id, ammo)
