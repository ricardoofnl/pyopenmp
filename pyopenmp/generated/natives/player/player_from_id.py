import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_FromID", ctypes.c_void_p, [ctypes.c_int])


def player_from_id(playerid):
    return _fn(playerid)
