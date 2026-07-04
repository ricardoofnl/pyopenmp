import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetCameraTargetPlayerObject", ctypes.c_void_p, [ctypes.c_void_p])


def player_get_camera_target_player_object(player):
    return _fn(player)
