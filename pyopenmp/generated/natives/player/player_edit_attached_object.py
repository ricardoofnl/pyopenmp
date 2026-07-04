import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_EditAttachedObject", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def player_edit_attached_object(player, index):
    return _fn(player, index)
