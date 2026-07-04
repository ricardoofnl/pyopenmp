import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Class_Add", ctypes.c_void_p, [ctypes.c_uint8, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint32, ctypes.POINTER(ctypes.c_int)])


def class_add(team, skin, x, y, z, angle, weapon1, ammo1, weapon2, ammo2, weapon3, ammo3):
    id = ctypes.c_int()
    __ret = _fn(team, skin, x, y, z, angle, weapon1, ammo1, weapon2, ammo2, weapon3, ammo3, ctypes.byref(id))
    return (__ret, id.value)
