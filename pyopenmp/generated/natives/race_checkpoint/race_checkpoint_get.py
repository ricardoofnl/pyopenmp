import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("RaceCheckpoint_Get", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def race_checkpoint_get(player):
    x = ctypes.c_float()
    y = ctypes.c_float()
    z = ctypes.c_float()
    next_x = ctypes.c_float()
    next_y = ctypes.c_float()
    next_z = ctypes.c_float()
    radius = ctypes.c_float()
    __ret = _fn(player, ctypes.byref(x), ctypes.byref(y), ctypes.byref(z), ctypes.byref(next_x), ctypes.byref(next_y), ctypes.byref(next_z), ctypes.byref(radius))
    if __ret:
        return (x.value, y.value, z.value, next_x.value, next_y.value, next_z.value, radius.value)
    return None
