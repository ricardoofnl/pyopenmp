import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Menu_IsDisabled", ctypes.c_bool, [ctypes.c_void_p])


def menu_is_disabled(menu):
    return _fn(menu)
