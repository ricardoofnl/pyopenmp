import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_IsReloading", ctypes.c_bool, [ctypes.c_void_p])


def npc_is_reloading(npc):
    return _fn(npc)
