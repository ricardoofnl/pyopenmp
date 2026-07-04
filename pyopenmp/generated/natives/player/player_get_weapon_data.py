import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetWeaponData", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)])


def player_get_weapon_data(player, slot):
    weaponid = ctypes.c_int()
    ammo = ctypes.c_int()
    __ret = _fn(player, slot, ctypes.byref(weaponid), ctypes.byref(ammo))
    if __ret:
        return (weaponid.value, ammo.value)
    return None
