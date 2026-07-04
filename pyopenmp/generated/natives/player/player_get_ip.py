import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetIp", ctypes.c_int, [ctypes.c_void_p, ctypes.POINTER(_capi.CAPIStringBuffer)])


def player_get_ip(player):
    ip = _capi.OutBuffer()
    __ret = _fn(player, ctypes.byref(ip.raw))
    return ip.value()
