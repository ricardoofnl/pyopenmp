import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_GetAttachedData", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)])


def object_get_attached_data(object):
    parent_vehicle = ctypes.c_int()
    parent_object = ctypes.c_int()
    parent_player = ctypes.c_int()
    __ret = _fn(object, ctypes.byref(parent_vehicle), ctypes.byref(parent_object), ctypes.byref(parent_player))
    if __ret:
        return (parent_vehicle.value, parent_object.value, parent_player.value)
    return None
