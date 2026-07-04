import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_RemovePointFromPath", ctypes.c_bool, [ctypes.c_int, ctypes.c_int])


def npc_remove_point_from_path(path_id, point_index):
    return _fn(path_id, point_index)
