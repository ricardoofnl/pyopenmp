import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextLabel_GetLOS", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def player_text_label_get_los(player, textlabel):
    return _fn(player, textlabel)
