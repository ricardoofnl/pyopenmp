import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_EnableReloading", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_bool])


def npc_enable_reloading(npc, enable):
    return _fn(npc, enable)
