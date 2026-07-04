import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Menu_GetItems", ctypes.c_int, [ctypes.c_void_p, ctypes.c_int])


def menu_get_items(menu, column):
    return _fn(menu, column)
