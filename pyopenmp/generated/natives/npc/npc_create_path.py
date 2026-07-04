import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_CreatePath", ctypes.c_int, [])


def npc_create_path():
    return _fn()
