import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_ClearAnimations", ctypes.c_bool, [ctypes.c_void_p])


def npc_clear_animations(npc):
    return _fn(npc)
