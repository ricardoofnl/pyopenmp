import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Dialog_Hide", ctypes.c_bool, [ctypes.c_void_p])


def dialog_hide(player):
    return _fn(player)
