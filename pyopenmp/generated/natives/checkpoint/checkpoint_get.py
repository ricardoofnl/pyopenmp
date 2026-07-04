import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Checkpoint_Get", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def checkpoint_get(player):
    x = ctypes.c_float()
    y = ctypes.c_float()
    z = ctypes.c_float()
    radius = ctypes.c_float()
    __ret = _fn(player, ctypes.byref(x), ctypes.byref(y), ctypes.byref(z), ctypes.byref(radius))
    if __ret:
        return (x.value, y.value, z.value, radius.value)
    return None
