import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("All_SendClientMessage", ctypes.c_bool, [ctypes.c_uint32, ctypes.c_char_p])


def all_send_client_message(color, text):
    return _fn(color, _capi.enc(text))
