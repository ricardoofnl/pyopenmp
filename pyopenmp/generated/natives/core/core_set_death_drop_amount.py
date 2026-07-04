import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_SetDeathDropAmount", ctypes.c_bool, [ctypes.c_int])


def core_set_death_drop_amount(amount):
    return _fn(amount)
