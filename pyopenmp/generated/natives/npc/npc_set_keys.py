import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetKeys", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16])


def npc_set_keys(npc, up_and_down, left_and_right, keys):
    return _fn(npc, up_and_down, left_and_right, keys)
