import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetSpawnInfo", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint32)])


def player_get_spawn_info(player):
    team = ctypes.c_uint8()
    skin = ctypes.c_int()
    x = ctypes.c_float()
    y = ctypes.c_float()
    z = ctypes.c_float()
    angle = ctypes.c_float()
    weapon1 = ctypes.c_uint8()
    ammo1 = ctypes.c_uint32()
    weapon2 = ctypes.c_uint8()
    ammo2 = ctypes.c_uint32()
    weapon3 = ctypes.c_uint8()
    ammo3 = ctypes.c_uint32()
    __ret = _fn(player, ctypes.byref(team), ctypes.byref(skin), ctypes.byref(x), ctypes.byref(y), ctypes.byref(z), ctypes.byref(angle), ctypes.byref(weapon1), ctypes.byref(ammo1), ctypes.byref(weapon2), ctypes.byref(ammo2), ctypes.byref(weapon3), ctypes.byref(ammo3))
    if __ret:
        return (team.value, skin.value, x.value, y.value, z.value, angle.value, weapon1.value, ammo1.value, weapon2.value, ammo2.value, weapon3.value, ammo3.value)
    return None
