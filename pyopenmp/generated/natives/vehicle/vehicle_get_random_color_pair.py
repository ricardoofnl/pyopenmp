import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetRandomColorPair", ctypes.c_bool, [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)])


def vehicle_get_random_color_pair(modelid):
    color1 = ctypes.c_int()
    color2 = ctypes.c_int()
    color3 = ctypes.c_int()
    color4 = ctypes.c_int()
    __ret = _fn(modelid, ctypes.byref(color1), ctypes.byref(color2), ctypes.byref(color3), ctypes.byref(color4))
    if __ret:
        return (color1.value, color2.value, color3.value, color4.value)
    return None
