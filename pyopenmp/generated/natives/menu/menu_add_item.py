import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Menu_AddItem", ctypes.c_int, [ctypes.c_void_p, ctypes.c_uint8, ctypes.c_char_p])


def menu_add_item(menu, column, text):
    return _fn(menu, column, _capi.enc(text))
