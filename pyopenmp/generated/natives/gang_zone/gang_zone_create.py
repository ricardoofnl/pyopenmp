import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("GangZone_Create", ctypes.c_void_p, [ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.POINTER(ctypes.c_int)])


def gang_zone_create(minx, miny, maxx, maxy):
    id = ctypes.c_int()
    __ret = _fn(minx, miny, maxx, maxy, ctypes.byref(id))
    return (__ret, id.value)
