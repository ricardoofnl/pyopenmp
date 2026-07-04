import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetPathCount", ctypes.c_int, [])


def npc_get_path_count():
    return _fn()
