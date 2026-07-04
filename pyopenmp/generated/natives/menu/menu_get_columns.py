import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Menu_GetColumns", ctypes.c_int, [ctypes.c_void_p])


def menu_get_columns(menu):
    return _fn(menu)
