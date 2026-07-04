import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetModelInfo", ctypes.c_bool, [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def vehicle_get_model_info(vehiclemodel, infotype):
    x = ctypes.c_float()
    y = ctypes.c_float()
    z = ctypes.c_float()
    __ret = _fn(vehiclemodel, infotype, ctypes.byref(x), ctypes.byref(y), ctypes.byref(z))
    if __ret:
        return (x.value, y.value, z.value)
    return None
