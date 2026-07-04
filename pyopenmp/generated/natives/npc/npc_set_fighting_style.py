import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetFightingStyle", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def npc_set_fighting_style(npc, style):
    return _fn(npc, style)
