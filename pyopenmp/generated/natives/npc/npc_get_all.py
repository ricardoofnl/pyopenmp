import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetAll", ctypes.c_int, [ctypes.POINTER(ctypes.c_int), ctypes.c_int])


def npc_get_all(max_np_cs):
    npcs_arr = ctypes.c_int()
    __ret = _fn(ctypes.byref(npcs_arr), max_np_cs)
    return (__ret, npcs_arr.value)
