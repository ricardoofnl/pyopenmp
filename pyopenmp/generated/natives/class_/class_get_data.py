import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Class_GetData", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint32)])


def class_get_data(classptr):
    teamid = ctypes.c_uint8()
    skin = ctypes.c_int()
    x = ctypes.c_float()
    y = ctypes.c_float()
    z = ctypes.c_float()
    angle = ctypes.c_float()
    weapon1 = ctypes.c_uint8()
    weapon1_ammo = ctypes.c_uint32()
    weapon2 = ctypes.c_uint8()
    weapon2_ammo = ctypes.c_uint32()
    weapon3 = ctypes.c_uint8()
    weapon3_ammo = ctypes.c_uint32()
    __ret = _fn(classptr, ctypes.byref(teamid), ctypes.byref(skin), ctypes.byref(x), ctypes.byref(y), ctypes.byref(z), ctypes.byref(angle), ctypes.byref(weapon1), ctypes.byref(weapon1_ammo), ctypes.byref(weapon2), ctypes.byref(weapon2_ammo), ctypes.byref(weapon3), ctypes.byref(weapon3_ammo))
    if __ret:
        return (teamid.value, skin.value, x.value, y.value, z.value, angle.value, weapon1.value, weapon1_ammo.value, weapon2.value, weapon2_ammo.value, weapon3.value, weapon3_ammo.value)
    return None
