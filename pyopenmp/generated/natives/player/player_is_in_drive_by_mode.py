import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_IsInDriveByMode", ctypes.c_bool, [ctypes.c_void_p])


def player_is_in_drive_by_mode(player):
    return _fn(player)
