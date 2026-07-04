import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SendMessageToPlayer", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p])


def player_send_message_to_player(player, sender, message):
    return _fn(player, sender, _capi.enc(message))
