import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextLabel_SetDrawDistance", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float])


def text_label_set_draw_distance(textlabel, distance):
    return _fn(textlabel, distance)
