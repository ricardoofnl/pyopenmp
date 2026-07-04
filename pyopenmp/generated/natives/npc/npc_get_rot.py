import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetRot", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def npc_get_rot(npc):
    rx = ctypes.c_float()
    ry = ctypes.c_float()
    rz = ctypes.c_float()
    __ret = _fn(npc, ctypes.byref(rx), ctypes.byref(ry), ctypes.byref(rz))
    if __ret:
        return (rx.value, ry.value, rz.value)
    return None
