import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Actor_ApplyAnimation", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_float, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_int])


def actor_apply_animation(actor, name, library, delta, loop, lock_x, lock_y, freeze, time):
    return _fn(actor, _capi.enc(name), _capi.enc(library), delta, loop, lock_x, lock_y, freeze, time)
