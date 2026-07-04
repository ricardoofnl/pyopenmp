import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_NetStatsGetConnectedTime", ctypes.c_int, [ctypes.c_void_p])


def player_net_stats_get_connected_time(player):
    return _fn(player)
