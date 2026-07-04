import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_IsPlaybackPaused", ctypes.c_bool, [ctypes.c_void_p])


def npc_is_playback_paused(npc):
    return _fn(npc)
