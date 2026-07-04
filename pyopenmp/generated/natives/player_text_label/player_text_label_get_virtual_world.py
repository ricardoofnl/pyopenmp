import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextLabel_GetVirtualWorld", ctypes.c_int, [ctypes.c_void_p])


def player_text_label_get_virtual_world(player):
    return _fn(player)
