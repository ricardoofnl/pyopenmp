import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_StopPlayback", ctypes.c_bool, [ctypes.c_void_p])


def npc_stop_playback(npc):
    return _fn(npc)
