import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetTime", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)])


def player_get_time(player):
    hour = ctypes.c_int()
    minute = ctypes.c_int()
    __ret = _fn(player, ctypes.byref(hour), ctypes.byref(minute))
    if __ret:
        return (hour.value, minute.value)
    return None
