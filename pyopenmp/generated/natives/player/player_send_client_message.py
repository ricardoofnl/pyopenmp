import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SendClientMessage", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_char_p])


def player_send_client_message(player, color, text):
    return _fn(player, color, _capi.enc(text))
