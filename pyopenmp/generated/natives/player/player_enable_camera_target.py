import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_EnableCameraTarget", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_bool])


def player_enable_camera_target(player, enable):
    return _fn(player, enable)
