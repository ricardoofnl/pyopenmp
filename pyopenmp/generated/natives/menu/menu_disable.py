import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Menu_Disable", ctypes.c_bool, [ctypes.c_void_p])


def menu_disable(menu):
    return _fn(menu)
