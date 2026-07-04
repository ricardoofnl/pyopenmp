import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetSkillLevel", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_uint8, ctypes.c_int])


def player_set_skill_level(player, weapon, level):
    return _fn(player, weapon, level)
