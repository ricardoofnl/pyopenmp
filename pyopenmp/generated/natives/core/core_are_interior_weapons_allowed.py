import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_AreInteriorWeaponsAllowed", ctypes.c_bool, [])


def core_are_interior_weapons_allowed():
    return _fn()
