import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_IsValidRecord", ctypes.c_bool, [ctypes.c_int])


def npc_is_valid_record(record_id):
    return _fn(record_id)
