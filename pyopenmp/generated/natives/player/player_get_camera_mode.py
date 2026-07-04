import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetCameraMode", ctypes.c_int, [ctypes.c_void_p])


def player_get_camera_mode(player):
    return _fn(player)
