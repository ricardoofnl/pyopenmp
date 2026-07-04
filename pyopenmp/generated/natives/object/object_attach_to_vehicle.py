import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_AttachToVehicle", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def object_attach_to_vehicle(object, vehicle, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z):
    return _fn(object, vehicle, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z)
