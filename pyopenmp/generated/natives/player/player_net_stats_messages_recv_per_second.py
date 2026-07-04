import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_NetStatsMessagesRecvPerSecond", ctypes.c_int, [ctypes.c_void_p])


def player_net_stats_messages_recv_per_second(player):
    return _fn(player)
