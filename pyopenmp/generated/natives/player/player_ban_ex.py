import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_BanEx", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_char_p])


def player_ban_ex(player, reason):
    return _fn(player, _capi.enc(reason))
