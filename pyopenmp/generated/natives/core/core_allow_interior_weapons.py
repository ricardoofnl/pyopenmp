import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_AllowInteriorWeapons", ctypes.c_bool, [ctypes.c_bool])


def core_allow_interior_weapons(allow):
    return _fn(allow)
