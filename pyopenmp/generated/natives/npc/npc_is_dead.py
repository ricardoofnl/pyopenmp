import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_IsDead", ctypes.c_bool, [ctypes.c_void_p])


def npc_is_dead(npc):
    return _fn(npc)
