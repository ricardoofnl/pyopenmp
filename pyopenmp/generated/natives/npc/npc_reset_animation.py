import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_ResetAnimation", ctypes.c_bool, [ctypes.c_void_p])


def npc_reset_animation(npc):
    return _fn(npc)
