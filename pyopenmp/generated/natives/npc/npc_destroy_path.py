import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_DestroyPath", ctypes.c_bool, [ctypes.c_int])


def npc_destroy_path(path_id):
    return _fn(path_id)
