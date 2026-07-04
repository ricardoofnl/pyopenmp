import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetKeys", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint16), ctypes.POINTER(ctypes.c_uint16), ctypes.POINTER(ctypes.c_uint16)])


def npc_get_keys(npc):
    up_and_down = ctypes.c_uint16()
    left_and_right = ctypes.c_uint16()
    keys = ctypes.c_uint16()
    __ret = _fn(npc, ctypes.byref(up_and_down), ctypes.byref(left_and_right), ctypes.byref(keys))
    if __ret:
        return (up_and_down.value, left_and_right.value, keys.value)
    return None
