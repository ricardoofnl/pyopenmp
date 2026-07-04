import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_PausePlayback", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_bool])


def npc_pause_playback(npc, paused):
    return _fn(npc, paused)
