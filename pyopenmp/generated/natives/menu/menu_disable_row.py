import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Menu_DisableRow", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_uint8])


def menu_disable_row(menu, row):
    return _fn(menu, row)
