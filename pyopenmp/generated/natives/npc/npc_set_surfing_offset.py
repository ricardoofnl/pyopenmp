import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetSurfingOffset", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def npc_set_surfing_offset(npc, x, y, z):
    return _fn(npc, x, y, z)
