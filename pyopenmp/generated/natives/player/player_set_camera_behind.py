import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetCameraBehind", ctypes.c_bool, [ctypes.c_void_p])


def player_set_camera_behind(player):
    return _fn(player)
