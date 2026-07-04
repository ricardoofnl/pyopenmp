import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_ResetSurfingData", ctypes.c_bool, [ctypes.c_void_p])


def npc_reset_surfing_data(npc):
    return _fn(npc)
