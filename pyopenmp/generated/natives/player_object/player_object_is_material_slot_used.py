import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerObject_IsMaterialSlotUsed", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int])


def player_object_is_material_slot_used(player, object, material_index):
    return _fn(player, object, material_index)
