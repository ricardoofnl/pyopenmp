import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_BlockIpAddress", ctypes.c_bool, [ctypes.c_char_p, ctypes.c_int])


def core_block_ip_address(ip_address, time_ms):
    return _fn(_capi.enc(ip_address), time_ms)
