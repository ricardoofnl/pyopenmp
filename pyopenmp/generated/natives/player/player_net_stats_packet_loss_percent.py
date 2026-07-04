import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_NetStatsPacketLossPercent", ctypes.c_float, [ctypes.c_void_p])


def player_net_stats_packet_loss_percent(player):
    return _fn(player)
