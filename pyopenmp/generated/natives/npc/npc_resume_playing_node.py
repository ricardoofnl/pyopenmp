import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_ResumePlayingNode", ctypes.c_bool, [ctypes.c_void_p])


def npc_resume_playing_node(npc):
    return _fn(npc)
