import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextLabel_GetDrawDistance", ctypes.c_float, [ctypes.c_void_p, ctypes.c_void_p])


def player_text_label_get_draw_distance(player, textlabel):
    return _fn(player, textlabel)
