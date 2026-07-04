import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetCameraLookAt", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_int])


def player_set_camera_look_at(player, x, y, z, cut_type):
    return _fn(player, x, y, z, cut_type)
