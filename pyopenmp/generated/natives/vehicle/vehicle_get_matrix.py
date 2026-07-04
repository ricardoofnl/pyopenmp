import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetMatrix", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def vehicle_get_matrix(vehicle):
    right_x = ctypes.c_float()
    right_y = ctypes.c_float()
    right_z = ctypes.c_float()
    up_x = ctypes.c_float()
    up_y = ctypes.c_float()
    up_z = ctypes.c_float()
    at_x = ctypes.c_float()
    at_y = ctypes.c_float()
    at_z = ctypes.c_float()
    __ret = _fn(vehicle, ctypes.byref(right_x), ctypes.byref(right_y), ctypes.byref(right_z), ctypes.byref(up_x), ctypes.byref(up_y), ctypes.byref(up_z), ctypes.byref(at_x), ctypes.byref(at_y), ctypes.byref(at_z))
    if __ret:
        return (right_x.value, right_y.value, right_z.value, up_x.value, up_y.value, up_z.value, at_x.value, at_y.value, at_z.value)
    return None
