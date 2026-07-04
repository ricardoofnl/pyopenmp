import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetWorldBounds", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def player_get_world_bounds(player):
    xmax = ctypes.c_float()
    xmin = ctypes.c_float()
    ymax = ctypes.c_float()
    ymin = ctypes.c_float()
    __ret = _fn(player, ctypes.byref(xmax), ctypes.byref(xmin), ctypes.byref(ymax), ctypes.byref(ymin))
    if __ret:
        return (xmax.value, xmin.value, ymax.value, ymin.value)
    return None
