import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetSurfingObject", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def npc_set_surfing_object(npc, object):
    return _fn(npc, object)
