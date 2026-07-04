import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_IsPlayerAttachedObjectSlotUsed", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def player_is_player_attached_object_slot_used(player, index):
    return _fn(player, index)
