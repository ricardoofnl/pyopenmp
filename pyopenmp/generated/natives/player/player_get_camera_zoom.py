import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetCameraZoom", ctypes.c_float, [ctypes.c_void_p])


def player_get_camera_zoom(player):
    return _fn(player)
