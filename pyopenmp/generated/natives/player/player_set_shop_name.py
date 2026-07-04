import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetShopName", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_char_p])


def player_set_shop_name(player, name):
    return _fn(player, _capi.enc(name))
