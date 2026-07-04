import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Menu_IsRowDisabled", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def menu_is_row_disabled(menu, row):
    return _fn(menu, row)
