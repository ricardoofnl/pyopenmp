import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_UnBlockIpAddress", ctypes.c_bool, [ctypes.c_char_p])


def core_un_block_ip_address(ip_address):
    return _fn(_capi.enc(ip_address))
