import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextLabel_Destroy", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def player_text_label_destroy(player, textlabel):
    return _fn(player, textlabel)
