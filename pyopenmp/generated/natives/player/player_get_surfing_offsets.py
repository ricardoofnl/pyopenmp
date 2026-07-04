import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetSurfingOffsets", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def player_get_surfing_offsets(player):
    offset_x = ctypes.c_float()
    offset_y = ctypes.c_float()
    offset_z = ctypes.c_float()
    __ret = _fn(player, ctypes.byref(offset_x), ctypes.byref(offset_y), ctypes.byref(offset_z))
    if __ret:
        return (offset_x.value, offset_y.value, offset_z.value)
    return None
