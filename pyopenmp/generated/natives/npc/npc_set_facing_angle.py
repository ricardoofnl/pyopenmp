import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetFacingAngle", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float])


def npc_set_facing_angle(npc, angle):
    return _fn(npc, angle)
