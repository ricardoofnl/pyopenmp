import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetAnimation", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_int)])


def npc_get_animation(npc):
    animation_id = ctypes.c_int()
    delta = ctypes.c_float()
    loop = ctypes.c_bool()
    lock_x = ctypes.c_bool()
    lock_y = ctypes.c_bool()
    freeze = ctypes.c_bool()
    time = ctypes.c_int()
    __ret = _fn(npc, ctypes.byref(animation_id), ctypes.byref(delta), ctypes.byref(loop), ctypes.byref(lock_x), ctypes.byref(lock_y), ctypes.byref(freeze), ctypes.byref(time))
    if __ret:
        return (animation_id.value, delta.value, loop.value, lock_x.value, lock_y.value, freeze.value, time.value)
    return None
