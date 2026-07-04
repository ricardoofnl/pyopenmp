import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_SetChatBubble", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_uint32, ctypes.c_float, ctypes.c_int])


def player_set_chat_bubble(player, text, color, drawdistance, expiretime):
    return _fn(player, _capi.enc(text), color, drawdistance, expiretime)
