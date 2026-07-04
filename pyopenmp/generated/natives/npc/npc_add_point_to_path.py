import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_AddPointToPath", ctypes.c_bool, [ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def npc_add_point_to_path(path_id, x, y, z, stop_range):
    return _fn(path_id, x, y, z, stop_range)
