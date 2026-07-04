import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetNetworkStats", ctypes.c_int, [ctypes.c_void_p, ctypes.POINTER(_capi.CAPIStringBuffer)])


def player_get_network_stats(player):
    output = _capi.OutBuffer()
    __ret = _fn(player, ctypes.byref(output.raw))
    return output.value()
