import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SendClientCheck", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int])


def player_send_client_check(player, action_type, address, offset, count):
    return _fn(player, action_type, address, offset, count)
