import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetRecordCount", ctypes.c_int, [])


def npc_get_record_count():
    return _fn()
