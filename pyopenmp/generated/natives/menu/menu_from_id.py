import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Menu_FromID", ctypes.c_void_p, [ctypes.c_int])


def menu_from_id(menuid):
    return _fn(menuid)
