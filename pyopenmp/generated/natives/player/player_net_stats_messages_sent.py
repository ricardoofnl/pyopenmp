import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_NetStatsMessagesSent", ctypes.c_int, [ctypes.c_void_p])


def player_net_stats_messages_sent(player):
    return _fn(player)
