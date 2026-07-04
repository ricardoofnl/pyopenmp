import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_ApplyAnimation", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_float, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_uint32, ctypes.c_int])


def player_apply_animation(player, animlib, animname, delta, loop, lock_x, lock_y, freeze, time, sync):
    return _fn(player, _capi.enc(animlib), _capi.enc(animname), delta, loop, lock_x, lock_y, freeze, time, sync)
