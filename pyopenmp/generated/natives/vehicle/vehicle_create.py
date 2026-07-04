import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_Create", ctypes.c_void_p, [ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_bool, ctypes.POINTER(ctypes.c_int)])


def vehicle_create(modelid, x, y, z, rotation, color1, color2, respawn_delay, add_siren):
    id = ctypes.c_int()
    __ret = _fn(modelid, x, y, z, rotation, color1, color2, respawn_delay, add_siren, ctypes.byref(id))
    return (__ret, id.value)
