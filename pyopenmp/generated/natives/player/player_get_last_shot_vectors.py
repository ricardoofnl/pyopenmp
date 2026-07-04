import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetLastShotVectors", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def player_get_last_shot_vectors(player):
    origin_x = ctypes.c_float()
    origin_y = ctypes.c_float()
    origin_z = ctypes.c_float()
    hit_x = ctypes.c_float()
    hit_y = ctypes.c_float()
    hit_z = ctypes.c_float()
    __ret = _fn(player, ctypes.byref(origin_x), ctypes.byref(origin_y), ctypes.byref(origin_z), ctypes.byref(hit_x), ctypes.byref(hit_y), ctypes.byref(hit_z))
    if __ret:
        return (origin_x.value, origin_y.value, origin_z.value, hit_x.value, hit_y.value, hit_z.value)
    return None
