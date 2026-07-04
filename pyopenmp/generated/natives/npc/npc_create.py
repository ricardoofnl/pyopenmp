import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_Create", ctypes.c_void_p, [ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)])


def npc_create(name):
    id = ctypes.c_int()
    __ret = _fn(_capi.enc(name), ctypes.byref(id))
    return (__ret, id.value)
