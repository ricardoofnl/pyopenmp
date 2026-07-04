import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SendDeathMessage", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int])


def player_send_death_message(player, killer, killee, weapon):
    return _fn(player, killer, killee, weapon)
