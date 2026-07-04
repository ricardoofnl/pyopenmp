import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Menu_Destroy", ctypes.c_bool, [ctypes.c_void_p])


def menu_destroy(menu):
    return _fn(menu)
