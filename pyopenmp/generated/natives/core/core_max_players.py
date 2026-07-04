import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_MaxPlayers", ctypes.c_int, [])


def core_max_players():
    return _fn()
