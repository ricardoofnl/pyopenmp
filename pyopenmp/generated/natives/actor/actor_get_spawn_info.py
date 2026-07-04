import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Actor_GetSpawnInfo", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_int)])


def actor_get_spawn_info(actor):
    x = ctypes.c_float()
    y = ctypes.c_float()
    z = ctypes.c_float()
    angle = ctypes.c_float()
    skin = ctypes.c_int()
    __ret = _fn(actor, ctypes.byref(x), ctypes.byref(y), ctypes.byref(z), ctypes.byref(angle), ctypes.byref(skin))
    if __ret:
        return (x.value, y.value, z.value, angle.value, skin.value)
    return None
