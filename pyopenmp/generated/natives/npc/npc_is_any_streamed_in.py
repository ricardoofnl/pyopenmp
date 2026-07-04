import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_IsAnyStreamedIn", ctypes.c_bool, [ctypes.c_void_p])


def npc_is_any_streamed_in(npc):
    return _fn(npc)
