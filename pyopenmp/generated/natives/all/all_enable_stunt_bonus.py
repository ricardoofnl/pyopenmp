import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("All_EnableStuntBonus", ctypes.c_bool, [ctypes.c_bool])


def all_enable_stunt_bonus(enable):
    return _fn(enable)
