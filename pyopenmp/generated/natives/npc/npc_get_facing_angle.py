import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetFacingAngle", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float)])


def npc_get_facing_angle(npc):
    angle = ctypes.c_float()
    __ret = _fn(npc, ctypes.byref(angle))
    if __ret:
        return angle.value
    return None
