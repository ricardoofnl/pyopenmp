import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("All_SendDeathMessage", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int])


def all_send_death_message(killer, killee, weapon):
    return _fn(killer, killee, weapon)
