import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Dialog_Show", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p])


def dialog_show(player, dialog, style, title, body, button1, button2):
    return _fn(player, dialog, style, _capi.enc(title), _capi.enc(body), _capi.enc(button1), _capi.enc(button2))
