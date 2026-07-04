import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_AttachToObject", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_bool])


def object_attach_to_object(object, obj_attached_to, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z, sync_rotation):
    return _fn(object, obj_attached_to, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z, sync_rotation)
