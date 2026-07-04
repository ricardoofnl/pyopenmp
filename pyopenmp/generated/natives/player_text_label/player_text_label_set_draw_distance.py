import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextLabel_SetDrawDistance", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float])


def player_text_label_set_draw_distance(player, textlabel, distance):
    return _fn(player, textlabel, distance)
