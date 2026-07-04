import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_DestroyAllPath", ctypes.c_bool, [])


def npc_destroy_all_path():
    return _fn()
