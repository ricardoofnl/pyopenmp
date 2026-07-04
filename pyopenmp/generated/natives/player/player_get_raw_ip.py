import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetRawIp", ctypes.c_uint32, [ctypes.c_void_p])


def player_get_raw_ip(player):
    return _fn(player)
