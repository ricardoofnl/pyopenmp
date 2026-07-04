import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_LoadRecord", ctypes.c_int, [ctypes.c_char_p])


def npc_load_record(file_path):
    return _fn(_capi.enc(file_path))
