import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetPathPoint", ctypes.c_bool, [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def npc_get_path_point(path_id, point_index):
    x = ctypes.c_float()
    y = ctypes.c_float()
    z = ctypes.c_float()
    stop_range = ctypes.c_float()
    __ret = _fn(path_id, point_index, ctypes.byref(x), ctypes.byref(y), ctypes.byref(z), ctypes.byref(stop_range))
    if __ret:
        return (x.value, y.value, z.value, stop_range.value)
    return None
