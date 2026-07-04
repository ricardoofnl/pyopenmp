import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetSkillLevel", ctypes.c_int, [ctypes.c_void_p, ctypes.c_int])


def player_get_skill_level(player, skill):
    return _fn(player, skill)
