import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Menu_SetColumnHeader", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_uint8, ctypes.c_char_p])


def menu_set_column_header(menu, column, header_title):
    return _fn(menu, column, _capi.enc(header_title))
