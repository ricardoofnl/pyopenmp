import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_IsMoving", ctypes.c_bool, [ctypes.c_void_p])


def npc_is_moving(npc):
    return _fn(npc)
