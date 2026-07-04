import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetRot", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def npc_set_rot(npc, rx, ry, rz):
    return _fn(npc, rx, ry, rz)
