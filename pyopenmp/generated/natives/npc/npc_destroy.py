import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_Destroy", ctypes.c_bool, [ctypes.c_void_p])


def npc_destroy(npc):
    return _fn(npc)
