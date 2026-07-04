import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetMapIcon", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_int, ctypes.c_uint32, ctypes.c_int])


def player_set_map_icon(player, icon_id, x, y, z, type, color, style):
    return _fn(player, icon_id, x, y, z, type, color, style)
