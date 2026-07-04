import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_IsReloadEnabled", ctypes.c_bool, [ctypes.c_void_p])


def npc_is_reload_enabled(npc):
    return _fn(npc)
