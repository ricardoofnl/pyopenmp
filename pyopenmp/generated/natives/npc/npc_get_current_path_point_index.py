import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetCurrentPathPointIndex", ctypes.c_int, [ctypes.c_void_p])


def npc_get_current_path_point_index(npc):
    return _fn(npc)
