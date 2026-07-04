import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_IsIpAddressBanned", ctypes.c_bool, [ctypes.c_char_p])


def core_is_ip_address_banned(ip):
    return _fn(_capi.enc(ip))
