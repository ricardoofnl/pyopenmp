import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_Connect", ctypes.c_bool, [ctypes.c_char_p, ctypes.c_char_p])


def npc_connect(name, script):
    return _fn(_capi.enc(name), _capi.enc(script))
