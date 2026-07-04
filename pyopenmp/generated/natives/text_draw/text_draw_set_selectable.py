import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_SetSelectable", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_bool])


def text_draw_set_selectable(textdraw, set):
    return _fn(textdraw, set)
