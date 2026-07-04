import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextDraw_SetSelectable", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool])


def player_text_draw_set_selectable(player, textdraw, set):
    return _fn(player, textdraw, set)
