import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetRotationQuat", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def player_get_rotation_quat(player):
    x = ctypes.c_float()
    y = ctypes.c_float()
    z = ctypes.c_float()
    w = ctypes.c_float()
    __ret = _fn(player, ctypes.byref(x), ctypes.byref(y), ctypes.byref(z), ctypes.byref(w))
    if __ret:
        return (x.value, y.value, z.value, w.value)
    return None
