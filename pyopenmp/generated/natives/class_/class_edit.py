import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Class_Edit", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_uint8, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint32])


def class_edit(classptr, teamid, skin, x, y, z, angle, weapon1, ammo1, weapon2, ammo2, weapon3, ammo3):
    return _fn(classptr, teamid, skin, x, y, z, angle, weapon1, ammo1, weapon2, ammo2, weapon3, ammo3)
