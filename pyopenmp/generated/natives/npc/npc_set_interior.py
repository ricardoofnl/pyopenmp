import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetInterior", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def npc_set_interior(npc, interior):
    return _fn(npc, interior)
