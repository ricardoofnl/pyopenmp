import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("GangZone_GetPos", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def gang_zone_get_pos(gangzone):
    minx = ctypes.c_float()
    miny = ctypes.c_float()
    maxx = ctypes.c_float()
    maxy = ctypes.c_float()
    __ret = _fn(gangzone, ctypes.byref(minx), ctypes.byref(miny), ctypes.byref(maxx), ctypes.byref(maxy))
    if __ret:
        return (minx.value, miny.value, maxx.value, maxy.value)
    return None
