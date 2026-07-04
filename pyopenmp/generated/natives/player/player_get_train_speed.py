import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetTrainSpeed", ctypes.c_float, [ctypes.c_void_p])


def player_get_train_speed(player):
    return _fn(player)
