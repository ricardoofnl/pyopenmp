import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetSpecialAction", ctypes.c_int, [ctypes.c_void_p])


def npc_get_special_action(npc):
    return _fn(npc)
