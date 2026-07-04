import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_HasPathPointInRange", ctypes.c_bool, [ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def npc_has_path_point_in_range(path_id, x, y, z, radius):
    return _fn(path_id, x, y, z, radius)
