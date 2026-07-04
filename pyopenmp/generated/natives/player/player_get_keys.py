import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetKeys", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)])


def player_get_keys(player):
    keys = ctypes.c_int()
    updown = ctypes.c_int()
    leftright = ctypes.c_int()
    __ret = _fn(player, ctypes.byref(keys), ctypes.byref(updown), ctypes.byref(leftright))
    if __ret:
        return (keys.value, updown.value, leftright.value)
    return None
