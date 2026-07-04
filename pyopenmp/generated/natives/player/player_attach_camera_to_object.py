import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_AttachCameraToObject", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def player_attach_camera_to_object(player, object):
    return _fn(player, object)
