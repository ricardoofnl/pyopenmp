import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetSkin", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def npc_set_skin(npc, model):
    return _fn(npc, model)
