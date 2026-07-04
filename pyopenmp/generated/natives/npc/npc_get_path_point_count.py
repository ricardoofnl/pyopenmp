import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetPathPointCount", ctypes.c_int, [ctypes.c_int])


def npc_get_path_point_count(path_id):
    return _fn(path_id)
