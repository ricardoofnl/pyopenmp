import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_NetStatsConnectionStatus", ctypes.c_int, [ctypes.c_void_p])


def player_net_stats_connection_status(player):
    return _fn(player)
