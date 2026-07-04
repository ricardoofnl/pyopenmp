import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_GetRot", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def object_get_rot(object):
    rotation_x = ctypes.c_float()
    rotation_y = ctypes.c_float()
    rotation_z = ctypes.c_float()
    __ret = _fn(object, ctypes.byref(rotation_x), ctypes.byref(rotation_y), ctypes.byref(rotation_z))
    if __ret:
        return (rotation_x.value, rotation_y.value, rotation_z.value)
    return None
