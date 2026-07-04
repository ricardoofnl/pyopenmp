import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_GetWeaponSlot", ctypes.c_int, [ctypes.c_uint8])


def core_get_weapon_slot(weapon):
    return _fn(weapon)
