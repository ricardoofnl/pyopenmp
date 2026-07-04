import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextLabel_AttachToVehicle", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def text_label_attach_to_vehicle(textlabel, vehicle, offset_x, offset_y, offset_z):
    return _fn(textlabel, vehicle, offset_x, offset_y, offset_z)
