import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetAttachedObject", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)])


def player_get_attached_object(player, index):
    modelid = ctypes.c_int()
    bone = ctypes.c_int()
    offset_x = ctypes.c_float()
    offset_y = ctypes.c_float()
    offset_z = ctypes.c_float()
    rotation_x = ctypes.c_float()
    rotation_y = ctypes.c_float()
    rotation_z = ctypes.c_float()
    scale_x = ctypes.c_float()
    scale_y = ctypes.c_float()
    scale_z = ctypes.c_float()
    materialcolor1 = ctypes.c_int()
    materialcolor2 = ctypes.c_int()
    __ret = _fn(player, index, ctypes.byref(modelid), ctypes.byref(bone), ctypes.byref(offset_x), ctypes.byref(offset_y), ctypes.byref(offset_z), ctypes.byref(rotation_x), ctypes.byref(rotation_y), ctypes.byref(rotation_z), ctypes.byref(scale_x), ctypes.byref(scale_y), ctypes.byref(scale_z), ctypes.byref(materialcolor1), ctypes.byref(materialcolor2))
    if __ret:
        return (modelid.value, bone.value, offset_x.value, offset_y.value, offset_z.value, rotation_x.value, rotation_y.value, rotation_z.value, scale_x.value, scale_y.value, scale_z.value, materialcolor1.value, materialcolor2.value)
    return None
