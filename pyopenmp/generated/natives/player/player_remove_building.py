import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_RemoveBuilding", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def player_remove_building(player, model, x, y, z, radius):
    return _fn(player, model, x, y, z, radius)
