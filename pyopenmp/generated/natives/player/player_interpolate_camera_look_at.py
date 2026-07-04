import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_InterpolateCameraLookAt", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_int, ctypes.c_int])


def player_interpolate_camera_look_at(player, from_x, from_y, from_z, to_x, to_y, to_z, time, cut):
    return _fn(player, from_x, from_y, from_z, to_x, to_y, to_z, time, cut)
