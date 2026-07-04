import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetSpawnInfo", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)])


def vehicle_get_spawn_info(vehicle):
    x = ctypes.c_float()
    y = ctypes.c_float()
    z = ctypes.c_float()
    rotation = ctypes.c_float()
    color1 = ctypes.c_int()
    color2 = ctypes.c_int()
    __ret = _fn(vehicle, ctypes.byref(x), ctypes.byref(y), ctypes.byref(z), ctypes.byref(rotation), ctypes.byref(color1), ctypes.byref(color2))
    if __ret:
        return (x.value, y.value, z.value, rotation.value, color1.value, color2.value)
    return None
