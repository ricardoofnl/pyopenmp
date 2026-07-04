import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextLabel_SetLOS", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool])


def player_text_label_set_los(player, textlabel, status):
    return _fn(player, textlabel, status)
