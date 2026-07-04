import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_GetWeaponName", ctypes.c_bool, [ctypes.c_int, ctypes.POINTER(_capi.CAPIStringView)])


def core_get_weapon_name(weaponid):
    output = _capi.CAPIStringView()
    __ret = _fn(weaponid, ctypes.byref(output))
    if __ret:
        return _capi.read_view(output)
    return None
