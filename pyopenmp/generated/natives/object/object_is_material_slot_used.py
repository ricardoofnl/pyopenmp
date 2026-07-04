import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_IsMaterialSlotUsed", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def object_is_material_slot_used(object, material_index):
    return _fn(object, material_index)
