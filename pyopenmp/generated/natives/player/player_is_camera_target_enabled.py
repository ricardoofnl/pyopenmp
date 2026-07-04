import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_IsCameraTargetEnabled", ctypes.c_bool, [ctypes.c_void_p])


def player_is_camera_target_enabled(player):
    return _fn(player)
