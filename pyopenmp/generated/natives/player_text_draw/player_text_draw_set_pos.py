import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextDraw_SetPos", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float])


def player_text_draw_set_pos(player, textdraw, x, y):
    return _fn(player, textdraw, x, y)
