import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_ClearBanList", ctypes.c_bool, [])


def core_clear_ban_list():
    return _fn()
