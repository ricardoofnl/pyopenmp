import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_NetworkStats", ctypes.c_int, [ctypes.POINTER(_capi.CAPIStringBuffer)])


def core_network_stats():
    output = _capi.OutBuffer()
    __ret = _fn(ctypes.byref(output.raw))
    return output.value()
