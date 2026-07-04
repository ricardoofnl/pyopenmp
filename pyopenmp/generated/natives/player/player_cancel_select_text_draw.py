import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_CancelSelectTextDraw", ctypes.c_bool, [ctypes.c_void_p])


def player_cancel_select_text_draw(player):
    return _fn(player)
