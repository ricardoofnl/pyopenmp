import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextLabel_GetID", ctypes.c_int, [ctypes.c_void_p, ctypes.c_void_p])


def player_text_label_get_id(player, textlabel):
    return _fn(player, textlabel)
