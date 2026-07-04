import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetVelocity", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def vehicle_get_velocity(vehicle):
    x = ctypes.c_float()
    y = ctypes.c_float()
    z = ctypes.c_float()
    __ret = _fn(vehicle, ctypes.byref(x), ctypes.byref(y), ctypes.byref(z))
    if __ret:
        return (x.value, y.value, z.value)
    return None
