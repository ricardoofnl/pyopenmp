import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_AddStatic", ctypes.c_void_p, [ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int)])


def vehicle_add_static(modelid, x, y, z, angle, color1, color2):
    id = ctypes.c_int()
    __ret = _fn(modelid, x, y, z, angle, color1, color2, ctypes.byref(id))
    return (__ret, id.value)
