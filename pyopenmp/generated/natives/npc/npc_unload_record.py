import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_UnloadRecord", ctypes.c_bool, [ctypes.c_int])


def npc_unload_record(record_id):
    return _fn(record_id)
