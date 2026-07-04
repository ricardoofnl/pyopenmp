import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_UnloadAllRecords", ctypes.c_bool, [])


def npc_unload_all_records():
    return _fn()
