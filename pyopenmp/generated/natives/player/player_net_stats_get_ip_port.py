import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_NetStatsGetIpPort", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(_capi.CAPIStringBuffer)])


def player_net_stats_get_ip_port(player):
    output = _capi.OutBuffer()
    __ret = _fn(player, ctypes.byref(output.raw))
    if __ret:
        return output.value()
    return None
