import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Actor_GetAnimation", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(_capi.CAPIStringView), ctypes.POINTER(_capi.CAPIStringView), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_int)])


def actor_get_animation(actor):
    library = _capi.CAPIStringView()
    name = _capi.CAPIStringView()
    delta = ctypes.c_float()
    loop = ctypes.c_bool()
    lock_x = ctypes.c_bool()
    lock_y = ctypes.c_bool()
    freeze = ctypes.c_bool()
    time = ctypes.c_int()
    __ret = _fn(actor, ctypes.byref(library), ctypes.byref(name), ctypes.byref(delta), ctypes.byref(loop), ctypes.byref(lock_x), ctypes.byref(lock_y), ctypes.byref(freeze), ctypes.byref(time))
    if __ret:
        return (_capi.read_view(library), _capi.read_view(name), delta.value, loop.value, lock_x.value, lock_y.value, freeze.value, time.value)
    return None
