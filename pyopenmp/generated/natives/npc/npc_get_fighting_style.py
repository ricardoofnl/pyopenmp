import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetFightingStyle", ctypes.c_int, [ctypes.c_void_p])


def npc_get_fighting_style(npc):
    return _fn(npc)
